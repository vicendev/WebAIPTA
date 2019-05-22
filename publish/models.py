from django.db import models
from publish.validators import validate_file_extension

# Create your models here.
class PDFPublish(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    image = models.ImageField(verbose_name="Imagen", upload_to="pdfImagen", null=True, blank=True)
    filepdf = models.FileField(verbose_name="Archivo PDF", upload_to="pdfpublish", validators=[validate_file_extension])
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha edición")

    class Meta:
        verbose_name = "revista"
        verbose_name_plural = "revistas"
        ordering = ['order','title']

    def __str__(self):
        return self.title