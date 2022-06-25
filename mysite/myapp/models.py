from django.db import models

'''
Defines the blueprint for the database tables of the application.
If we create a model , django will automatically create a table out of it.
'''
# Create your models here.
'''
Models are like the entity classes in Spring
'''

'''
To create a actual table out of the model we need to run command:
1. python manage.py makemigrations
2. python manage.py migrate
'''

'''
If we want to create a object of this model and put in the database table then we have to use shell of django 
to create a entry of the table.
'''


class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    book_image = models.ImageField(default='default.jpg', upload_to='media/book_images/')
    author = models.CharField(default='Mr. ABC', max_length=100)
    book_pdf = models.FileField(default='default.pdf', upload_to='media/book_pdf')
    genre = models.CharField(max_length=100, default='comedy')