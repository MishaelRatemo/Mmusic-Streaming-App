from django.db import models

# Create your models here.
class Registrations(models.Model):
    username = models.CharField(max_length=200, unique=True)
    userimage = models.ImageField(upload_to='profileimgs')
    passwords = models.CharField(max_length=300)
    roles = models.CharField(max_length=100, default='Not Admin')

    class Meta:
        db_table = 'Registrations'
    
    def __str__(self):
        return self.username