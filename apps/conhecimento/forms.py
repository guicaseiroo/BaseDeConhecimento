from django import forms
from django.utils.safestring import mark_safe

from .models import MeuModelo  # Substitua pelo nome correto do seu modelo


class CKEditor5Widget(forms.Textarea):
    class Media:
        # Usando a build do CKEditor 5 com todos os plugins via CDN
        js = ('https://cdn.ckeditor.com/ckeditor5/36.0.1/classic/ckeditor.js',)

    def render(self, name, value, attrs=None, renderer=None):
        # Renderiza o campo textarea padrão e insere o script do CKEditor 5 com configurações personalizadas
        text_area = super().render(name, value, attrs, renderer)
        return mark_safe(
            f"""
            {text_area}
            <script>
                ClassicEditor
                    .create(document.querySelector("#id_{name}"), {{
                        toolbar: [
                            'heading', '|', 'bold', 'italic', 'underline', 'strikethrough', 
                            'fontColor', 'fontBackgroundColor', 'fontSize', 'fontFamily', '|', 
                            'link', 'bulletedList', 'numberedList', 'blockQuote', 'insertTable', 
                            'tableColumn', 'tableRow', 'mergeTableCells', '|', 'undo', 'redo', 
                            'alignment', 'imageUpload', 'mediaEmbed', 'horizontalLine', 'specialCharacters'
                        ],
                        image: {{
                            toolbar: [ 'imageTextAlternative', 'imageStyle:full', 'imageStyle:side' ]
                        }},
                        table: {{
                            contentToolbar: [ 'tableColumn', 'tableRow', 'mergeTableCells' ]
                        }},
                        mediaEmbed: {{
                            previewsInData: true  // Permitir visualização de mídia embutida como YouTube
                        }},
                        height: 500,  // Altura do editor
                        link: {{
                            decorators: {{
                                addTargetToExternalLinks: true
                            }}
                        }},
                        heading: {{
                            options: [
                                { '{ model: "paragraph", title: "Paragraph", class: "ck-heading_paragraph" }' },
                                { '{ model: "heading1", view: "h1", title: "Heading 1", class: "ck-heading_heading1" }' },
                                { '{ model: "heading2", view: "h2", title: "Heading 2", class: "ck-heading_heading2" }' },
                                { '{ model: "heading3", view: "h3", title: "Heading 3", class: "ck-heading_heading3" }' }
                            ]
                        }},
                        fontFamily: {{
                            options: [
                                'default', 'Arial, Helvetica, sans-serif', 'Courier New, Courier, monospace', 
                                'Georgia, serif', 'Lucida Sans, Lucida Grande, sans-serif', 
                                'Tahoma, sans-serif', 'Times New Roman, Times, serif', 'Verdana, Geneva, sans-serif'
                            ]
                        }},
                        fontSize: {{
                            options: [ 'tiny', 'small', 'default', 'big', 'huge' ]
                        }},
                        alignment: {{
                            options: [ 'left', 'center', 'right', 'justify' ]
                        }}
                    }})
                    .catch(error => {{
                        console.error(error);
                    }});
            </script>
        """
        )


class MeuModeloForm(forms.ModelForm):
    texto = forms.CharField(
        widget=CKEditor5Widget()
    )  # Substitua 'texto' pelo nome correto do campo no seu modelo

    class Meta:
        model = MeuModelo  # Substitua pelo nome correto do seu modelo
        fields = '__all__'  # Inclua todos os campos do modelo
