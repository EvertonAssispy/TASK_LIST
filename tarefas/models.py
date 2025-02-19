from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class task(models.Model):
    # instancia para decisao
    STATUS = (
        ('doing', 'Doing'),
        ('done', 'Done'),    
    )
    
    titulo = models.CharField(max_length=50)
    tarefas = models.TextField() 
    done = models.CharField(
        max_length = 5,
        choices = STATUS,
    )
    '''Para adcionar um usuario precisamos da biblioteca get_user_model ja salvando numa foreingkey na variavel "usuario" '''
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.titulo


class myfoto(models.Model):
    titulo = models.CharField(max_length=20)
    foto = models.ImageField(upload_to="img") 
    
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo