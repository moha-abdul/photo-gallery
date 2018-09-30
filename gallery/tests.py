from django.test import TestCase

from .models import Photos, Category, Location

class TestCategory(TestCase):
    def setUp(self):
        '''
        Set up method for category
        '''
        self.abstract = Category(name='abstract')

    def test_instance(self):
        '''
        test of save method of category
        '''
        self.abstract.save()
        self.assertTrue(isinstance(self.abstract, Category))

class TestLocation(TestCase):
    def setUp(self):
        '''
        Set up method for location
        '''
        self.kenya = Location(location='kenya')

    def test_instance(self):
        '''
        test of save method of location
        '''
        self.kenya.save()
        self.assertTrue(isinstance(self.kenya, Location))

class TestPhotos(TestCase):
    def setUp(self):
        '''
        Set up method for photos
        '''
        self.lab = Photos(name='lab')

    def test_search_image(self):
        self.lab.save()
        images = Photos.search_image('lab')
        self.assertTrue(len(images) > 0)
