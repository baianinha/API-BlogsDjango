from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here. iremos criar um blog
# CharFildes sig. que podemos receber strings de até 255 caracteres

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    # www.meusite.com/blog/introdução-ao-django
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) # cada modificação que fizermos em um artigo o update vai atualizar automaticamente

    class Meta:
        ordering = ("-created",)
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blogs:detail", kwargs={"slug": self.slug})