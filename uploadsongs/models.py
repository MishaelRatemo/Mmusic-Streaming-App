from django.db import models
from signupforms.models import Registrations
# Create your models here.
class SongUploads(models.Model):
    artists = models.ForeignKey(Registrations, on_delete = models.CASCADE)
    songtitle = models.CharField(max_length=200)
    songalbum = models.CharField(max_length=200, default='Album A')
    songtype = models.CharField(max_length=100)
    songfile = models.FileField(upload_to='songs/')
    songlyrics = models.TextField(null=True)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'SongUploads'

    def __str__(self):
        return self.songtitle