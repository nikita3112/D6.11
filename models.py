from django.db import models

class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)
    photo = models.ImageField(upload_to="images/", null=True)

    def __str__(self):
        return self.full_name

class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    image = models.ImageField(upload_to="images/", null=True)
    title = models.TextField()
    description = models.TextField()
    copy_count = models.IntegerField(default=1)
    price = models.FloatField(default=0)
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title