from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    order = models.SmallIntegerField(verbose_name="order", default=0)
    content = RichTextField(verbose_name="Contenido")
    created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de actualización", auto_now=True)

    class Meta:
        verbose_name = "pagina"
        verbose_name_plural = "paginas"
        ordering = ["-order", "title"]

    def __str__(self) -> str:
        return self.title
