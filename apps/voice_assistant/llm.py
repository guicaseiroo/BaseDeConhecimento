import os
import requests
from bs4 import BeautifulSoup
from sklearn.neighbors import NearestNeighbors
import numpy as np
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
from openai import OpenAI
from conhecimento.models import MeuModelo

# Configuração da API OpenAI
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

class WebDocument:
    def __init__(self, content, metadata=None):
        self.page_content = content
        self.metadata = metadata if metadata is not None else {}

def scrape_web_links(links):
    documents = []
    for link in links:
        try:
            response = requests.get(link)
            soup = BeautifulSoup(response.content, 'html.parser')
            text = soup.get_text(separator=' ')
            documents.append(WebDocument(text, {'source': link}))
            print(f"Conteúdo coletado do link: {link}")
        except Exception as e:
            print(f"Erro ao coletar o link {link}: {e}")
    return documents

def load_pdfs(pdf_directory):
    documents = []
    for filename in os.listdir(pdf_directory):
        if filename.endswith('.pdf'):
            filepath = os.path.join(pdf_directory, filename)
            loader = PyPDFLoader(filepath)
            documents.extend(loader.load())
            print(f"Carregado {len(loader.load())} documentos de {filename}")
    return documents

class DjangoDocument:
    def __init__(self, content, metadata=None):
        self.page_content = content
        self.metadata = metadata if metadata is not None else {}

def load_from_database():
    documents = []
    registros = MeuModelo.objects.all()
    for registro in registros:
        documents.append(DjangoDocument(registro.texto, {'source': 'database'}))
    print(f"{len(documents)} documentos carregados do banco de dados.")
    return documents

# Função para criar o índice usando Scikit-learn NearestNeighbors
def create_sklearn_index(documents, embeddings):
    document_embeddings = []
    for doc in documents:
        vector = embeddings.embed_query(doc.page_content)
        document_embeddings.append(vector)
    
    # Convertendo para numpy array para o NearestNeighbors
    document_embeddings = np.array(document_embeddings)
    
    # Criando o índice com NearestNeighbors
    nn_model = NearestNeighbors(n_neighbors=3, algorithm='auto').fit(document_embeddings)
    
    return nn_model, document_embeddings

def load_and_index_content(pdf_directory, links):
    pdf_texts = load_pdfs(pdf_directory)
    web_texts = scrape_web_links(links)
    db_texts = load_from_database()
    
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    
    pdf_chunks = text_splitter.split_documents(pdf_texts)
    web_chunks = text_splitter.split_documents(web_texts)
    db_chunks = text_splitter.split_documents(db_texts)
    
    # Criando índices para cada conjunto de documentos
    pdf_index, pdf_embeddings = create_sklearn_index(pdf_chunks, embeddings)
    web_index, web_embeddings = create_sklearn_index(web_chunks, embeddings)
    db_index, db_embeddings = create_sklearn_index(db_chunks, embeddings)
    
    return pdf_index, web_index, db_index, pdf_embeddings, web_embeddings, db_embeddings

def query_knowledge_base(query, pdf_index, web_index, db_index, pdf_embeddings, web_embeddings, db_embeddings, prompt, history=[]):
    query_vector = embeddings.embed_query(query).reshape(1, -1)  # Vetor de consulta

    # Realizar buscas nos índices sklearn
    pdf_distances, pdf_ids = pdf_index.kneighbors(query_vector, n_neighbors=3)
    web_distances, web_ids = web_index.kneighbors(query_vector, n_neighbors=3)
    db_distances, db_ids = db_index.kneighbors(query_vector, n_neighbors=3)

    # Recuperar o conteúdo dos documentos a partir dos IDs
    pdf_docs = [pdf_embeddings[i] for i in pdf_ids[0]]
    web_docs = [web_embeddings[i] for i in web_ids[0]]
    db_docs = [db_embeddings[i] for i in db_ids[0]]
    
    combined_docs = pdf_docs + web_docs + db_docs
    if not combined_docs:
        return "Desculpe, mas os documentos fornecidos não contêm informações sobre a consulta."
    
    combined_content = " ".join([str(doc) for doc in combined_docs])
    
    history.append({"role": "user", "content": f"Documentos:\n{combined_content}\n\nConsulta: {query}"})
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": prompt}] + history,
        max_tokens=900,
        temperature=0,
        n=1,
        stop=None
    )
    
    reply = response.choices[0].message.content.strip()
    history.append({"role": "assistant", "content": reply})
    return reply
