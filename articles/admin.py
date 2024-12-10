from django.contrib import admin
from .models import Articles

# Register your models here.
# admin.site.register(Articles)

@admin.register(Articles)
class AdminArticle(admin.ModelAdmin):
    list_display = ['name','discription']
