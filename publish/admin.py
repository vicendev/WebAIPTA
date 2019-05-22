from django.contrib import admin
from publish.models import PDFPublish

# Register your models here.
class PDFPublishAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(PDFPublish, PDFPublishAdmin)