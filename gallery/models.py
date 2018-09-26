from django.db import models

class Photos(models.Model):
    photo = models.ImageField(upload_to='/media')
    name = models.CharField(max_length =60)
    description = models.TextField()

    def __str__(self):
        return self.name
