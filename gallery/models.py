from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

class Location(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
    
    def save_location(self):
        self.save()


class Photos(models.Model):
    photo = models.ImageField(upload_to='myphotos/')
    name = models.CharField(max_length =60)
    description = models.TextField()
    category = models.ForeignKey(Category, default=True)
    location = models.ForeignKey(Location, default=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update_image()

    def __str__(self):
        return self.name
    
    # @classmethod
    # def all_photos(cls):
    #     photos = Photos.objects.filter()
    #     return photos


