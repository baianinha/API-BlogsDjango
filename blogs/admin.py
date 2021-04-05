from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin): # podemos mudar os arquivos, fazer barra de buscas...
    list_display = ('title', 'slug', 'author', 'created', 'updated') #tupla
    prepopulated_fields = {'slug': ('title',)}# escreve o slug automaticamente

# Register your models here.
