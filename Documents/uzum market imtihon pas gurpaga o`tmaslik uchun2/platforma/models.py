from django.db import models

class Post(models.Model):
    img = models.ImageField()
    text = models.TextField()
    text2 = models.IntegerField( null=True )
    text3 = models.IntegerField(null=True)
    list_display = ('text', 'is_original')
    
    def __str__(self):
        return self.text

 

# Create your models here.
