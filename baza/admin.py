from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Reader


class ReaderResource(resources.ModelResource):

    class Meta:
        model = Reader
        fields = ('id', 'fio', 'eticket',)
        export_order = ('id', 'fio', 'eticket')


class ReaderAdmin(ImportExportModelAdmin):
    resource_class = ReaderResource


admin.site.register(Reader, ReaderAdmin)
