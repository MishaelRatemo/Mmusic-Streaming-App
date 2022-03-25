from django.db import models
from uploadsongs.models import SongUploads
# Create your models here.
class Favourites(models.Model):
    username = models.CharField(max_length=100)
    songfileid = models.ForeignKey(SongUploads, on_delete = models.CASCADE)

    class Meta:
        db_table ='Favourites'

    def __str__(self):
        return self.username