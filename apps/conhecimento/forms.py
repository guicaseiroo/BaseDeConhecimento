from ckeditor_uploader.widgets import CKEditorUploadingWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from .models import MeuModelo


class MeuModeloForm(forms.ModelForm):
    texto = forms.CharField(
        widget=CKEditorUploadingWidget(),
        required=False,  # Campo não obrigatório no formulário, já que será substituído pelo CKEditor
    )
    titulo = forms.CharField(max_length=255, label='Título')
    categorias = forms.CharField(max_length=150, label='Categorias')
    validade = forms.DateTimeField(label='Validade da Publicação')

    class Meta:
        model = MeuModelo
        fields = [
            'titulo',
            'categorias',
            'validade',
            'texto',
        ]  # Não inclui 'usuario_criador'

    def __init__(self, *args, **kwargs):
        super(MeuModeloForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
