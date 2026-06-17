from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField(default=0)
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=245)
    slug = models.SlugField(max_length=245)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    readtime = models.DurationField()

    def __str__(self):
        return self.title


class Club(models.Model):
    name = models.CharField(max_length=100)
    stadion = models.CharField(max_length=245)
    forma = models.CharField(max_length=245)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    position = models.CharField(max_length=245)
    number = models.IntegerField()
    club = models.ForeignKey(Club,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name

class Author(models.Model):

    jins_choice = (
        ("Erkak", "Erkak"),
        ("Ayol", "Ayol"),
    )

    name = models.CharField(max_length=100)
    jinsi = models.CharField(choices=jins_choice, max_length=245,blank=True, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=245)
    author = models.ManyToManyField(Author)

    def __str__(self):
        return self.name

class Notebook(models.Model):
    name = models.CharField(max_length=245)
    brand = models.CharField(max_length=245)
    ram = models.CharField(max_length=245)
    memory = models.CharField(max_length=245)
    video_card = models.CharField(max_length=245)

    def __str__(self):
        return self.name

