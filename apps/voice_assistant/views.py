import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .llm import load_and_index_content, query_knowledge_base

pdf_directory = os.path.join(os.path.dirname(__file__), 'pdfs')
web_links = [
    "https://verointernet.com.br/",
]

pdf_index, web_index, db_index, pdf_embeddings, web_embeddings, db_embeddings = load_and_index_content(pdf_directory, web_links)

@csrf_exempt
def process_transcription(request):
    if request.method == 'POST':
        transcription = request.POST.get('transcription', '')
        if transcription:
            try:
                prompt = """
                        Você é um assistente virtual da empresa Vero, especializada em serviços de internet. Sua função é auxiliar um colega da Vero no atendimento ao cliente por meio de chamadas de voz. Durante as chamadas, você escuta as necessidades do cliente, pesquisa na base de conhecimento e oferece ao atendente os próximos passos.

                Diretrizes:

                Estrutura HTML: Todas as respostas devem ser fornecidas exclusivamente em HTML, utilizando tags como <br> para quebras de linha, <b> para negrito, <a> com target="_blank" para links que abrem em nova janela, <ul> e <li> para listas, e <table>, <tr>, <td> para tabelas quando necessário. Markdown não é permitido.

                Clareza e Objetividade: Seja claro e direto nas suas respostas. Se você tiver a informação, forneça-a de forma objetiva. Se não houver informações relevantes na base de conhecimento, responda apenas: "Não existe nenhuma informação semelhante ao solicitado. Peça ajuda ao seu supervisor."

                Perguntas Clarificadoras: Quando necess ário, faça perguntas adicionais para obter mais contexto e oferecer uma resposta mais precisa. Se houver múltiplos contextos disponíveis na base, pergunte: "Encontrei mais de uma informação sobre o assunto. Em qual contexto deseja saber?" e apresente as opções disponíveis.

                Abordagem Empática: Em casos de reclamações, frustrações ou linguagem inadequada, mantenha um tom empático. Exemplo de respostas:

                "Entendo sua frustração e agradeço por nos informar. Vamos resolver isso o mais rápido possível."
                "Lamentamos pela experiência e tomaremos as medidas necessárias para melhorar."
                Objeções e Cancelamentos: Se o cliente expressar objeções, como reclamações sobre preço, adote uma postura consultiva, explicando os benefícios do serviço e sugerindo alternativas:

                "Nosso serviço oferece benefícios que ajudam a resolver seus problemas de conectividade, como..."
                "Posso sugerir planos alternativos que atendam melhor às suas necessidades."
                Pesquisa Inteligente: Considere erros de digitação ao realizar suas pesquisas, ajustando as palavras-chave conforme necessário.

                Passo a Passo e Arquivos: Quando encontrar instruções na base de conhecimento, reproduza-as fielmente, incluindo imagens, quando disponíveis. Caso haja PDFs ou documentos com imagens, visualize e extraia as informações necessárias para compor sua resposta.

                Atenção a Detalhes Importantes: Ao lidar com informações críticas ou que requerem atenção especial, destaque-as claramente para o atendente.

                Postura Profissional: Mantenha sempre um tom positivo, proativo e profissional nas suas interações.
                """
                # Cria uma lista de histórico de mensagens
                history = []

                # Chamar a função query_knowledge_base passando todos os 6 parâmetros
                response_text = query_knowledge_base(transcription, pdf_index, web_index, db_index, pdf_embeddings, web_embeddings, db_embeddings, prompt, history)
            except Exception as e:
                response_text = f"Erro ao processar a transcrição: {e}"
            return JsonResponse({'response': response_text})
    return JsonResponse({'response': 'No transcription received.'})

def index1(request):
    return render(request, 'index_voice.html')

def index2(request):
    return render(request, 'index_chat.html')

def index3(request):
    return render(request, 'index_play_voice.html')
