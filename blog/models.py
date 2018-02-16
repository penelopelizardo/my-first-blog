from django.db import models
from django.utils import timezone

#Mi clase
class Post(models.Model):
    #Mis atributos 
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    #Mis metodos
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
