from django.contrib import admin
from .models import Post

#Esto es para que me aparezca en admin, si lo quito no aparece. 
admin.site.register(Post)
