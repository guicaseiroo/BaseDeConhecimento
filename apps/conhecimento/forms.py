from ckeditor_uploader.widgets import CKEditorUploadingWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

from .models import MeuModelo  # Substitua pelo nome correto do seu modelo


class MeuModeloForm(forms.ModelForm):
    texto = forms.CharField(
        widget=CKEditorUploadingWidget()
    )  # Certifique-se de que o campo 'texto' está presente
    titulo = forms.CharField(max_length=255, label='Título')
    categorias = forms.CharField(max_length=150, label='Categorias')
    validade = forms.DateTimeField(label='Validade da Publicação')

    class Meta:
        model = MeuModelo
        # fields = ['titulo', 'categorias', 'validade', 'usuario_criador' ]  # Excluímos 'texto' nessa primeira parte
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MeuModeloForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Próximo: Editar Texto'))
