from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from web.models import user


@admin.register(user)
class userAdmin(ImportExportActionModelAdmin):
    list_display = ("id","name" , "phone", "email")
