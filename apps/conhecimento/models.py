from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

CATEGORIA_CHOICES = (
    ('1', 'Dúvidas'),
    ('2', 'Procedimentos'),
    ('3', 'Informações'),
    ('4', 'Benefícios'),
    ('5', 'Suporte Técnico'),
    ('6', 'Regras Comeciais'),
)


def validate_future_date(value):
    if value < timezone.now():
        raise ValidationError('A data deve estar no futuro.')


class MeuModelo(models.Model):
    titulo = models.CharField(
        max_length=255,
        verbose_name='Título',
    )
    categorias = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Categoriais',
    )
    texto = RichTextUploadingField()
    validade = models.DateTimeField(
        blank=True,
        null=True,
        validators=[validate_future_date],
        verbose_name='Validade da Publicação',
    )

    usuario_criador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    data_created = models.DateTimeField(
        auto_now_add=True,
    )
    data_updated = models.DateTimeField(
        auto_now=True,
    )

    def set_categorias(self, categorias_list):
        self.categorias = ','.join(categorias_list)

    def get_categorias(self):
        return self.categorias.split(',')

    def get_categoria_display(self):
        return [
            dict(CATEGORIA_CHOICES).get(categoria, categoria)
            for categoria in self.get_categorias()
        ]

    def __str__(self):
        return self.titulo
