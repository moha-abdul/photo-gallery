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

    def delete_category(self):
        '''
        method to save category
        '''
        self.delete()

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

    def delete_location(self):
        '''
        deletes an instance of the location
        '''
        self.delete()

    @classmethod
    def update_location(cls,id,update):
        location_update = cls.objects.filter(id=id).update(name=update)
        return location_update()



class Photos(models.Model):
    '''
    defines the Photos class
    '''
    photo = models.ImageField(upload_to='myphotos/')
    name = models.CharField(max_length =60)
    description = models.TextField()
    category = models.ForeignKey(Category, default=True)
    location = models.ForeignKey(Location, default=True)

    def save_photo(self):
        '''
        method to save photo
        '''
        self.save()

    def delete_photo(self):
        '''
        method to delete photo
        '''
        self.delete()

    def update_photo(self):
        '''
        method to update photo
        '''
        self.update_photo()

    def __str__(self):
        return self.name

    @classmethod
    def display_single_photo(cls, id):
        '''
        method to display single image
        '''
        photo = cls.objects.get(id=id)
        return photo

    @classmethod
    def search_photo(cls, search_term):
        '''
        method to display image that is searched using its name
        '''
        searched_photo = cls.objects.filter(name__icontains=search_term)
        return searched_photo

    @classmethod
    def search_by_category(cls,name):
        photos_category = cls.objects.filter(category__name__icontains=name)
        return photos_category


