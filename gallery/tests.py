from django.test import TestCase
from .models import Location, Photos, Category


# Create your tests here.
class LocationTest(TestCase):
    def setUp(self):
        self.test_location = Location(name='kenya')

    def test_instance(self):
        self.assertTrue(isinstance(self.test_location,Location))

    def test_data(self):
        self.assertTrue(self.test_location.name,"kenya")

    def test_save(self):
        self.test_location.save()
        location = Location.objects.all()
        self.assertTrue(len(location)>0)

    def test_delete(self):
        location = Location.objects.filter(id=1)
        location.delete()
        test = Location.objects.all()
        self.assertTrue(len(test) == 0)

    def test_update(self):
        self.test_location.save_location()
        self.update_locations = Location.objects.filter(name='uganda').update(name ='kenya')
        self.updated_locations = Location.objects.get(name='kenya')
        self.assertTrue(self.updated_locations.name,'kenya')


class CategoryTest(TestCase):
    def setUp(self):
        self.test_category = Category(name='nature')

    def test_instance(self):
        self.assertTrue(isinstance(self.test_category,Category))

    def test_data(self):
        self.assertTrue(self.test_category.name, "nature")

    def test_save(self):
        self.test_category.save()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete(self):
        category = Category.objects.filter(id=1)
        category.delete()
        cat = Category.objects.all()
        self.assertTrue(len(cat) == 0)

    def test_update_category(self):
        self.test_category.save()
        self.update_cat = Category.objects.filter(name='abstract').update(name='')
        self.updated_cat = Category.objects.get(name='nature')
        self.assertTrue(self.updated_cat.name, 'nature')

    def test_get_category_by_id(self):
        self.test_category.save()
        cat = Category.objects.get(id=1)
        self.assertTrue(cat.name, 'nature')


class PhotosTest(TestCase):
    def setUp(self):
        self.test_photo = Photos(name="lab", description="awesome")

    def test_instance(self):
        self.assertTrue(isinstance(self.test_photo,Photos))

    def test_data(self):
        self.assertTrue(self.test_photo.name,'lab')
        self.assertTrue(self.test_photo.description,'awesome')

    # def test_save(self):
    #     self.test_photo.save()
    #     photos = Photos.objects.all()
    #     self.assertTrue(len(photos)>0)

    def test_delete(self):
        photo = Photos.objects.filter(id=1)
        photo.delete()
        photos = Photos.objects.all()
        self.assertTrue(len(photos) == 0)