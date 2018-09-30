from django.db import models

class Category(models.Model):
    '''
    defines the Category class
    '''
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    def save_category(self):
        '''
        method to save category
        '''
        self.save()

class Location(models.Model):
    '''
    defines the Location class
    '''
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
    
    def save_location(self):
        '''
        saves an instance of the location
        '''
        self.save()


class Photos(models.Model):
    '''
    defines the Photos class
    '''
    photo = models.ImageField(upload_to='myphotos/')
    name = models.CharField(max_length =60)
    description = models.TextField()
    category = models.ForeignKey(Category, default=True)
    location = models.ForeignKey(Location, default=True)

    def save_image(self):
        '''
        method to save image
        '''
        self.save()

    def delete_image(self):
        '''
        method to delete image
        '''
        self.delete()

    def update_image(self):
        '''
        method to update image
        '''
        self.update_image()

    def __str__(self):
        return self.name

    @classmethod
    def display_single_image(cls, id):
        '''
        method to display single image
        '''
        photo = cls.objects.get(id=id)
        return photo

    @classmethod
    def search_image(cls, search_term):
        '''
        method to display image that is searched using its name
        '''
        searched_image = cls.objects.filter(name__icontains=search_term)
        return searched_image

    @classmethod
    def search_by_category(cls,name):
        images_category = cls.objects.filter(category__name__icontains=name)
        return images_category


