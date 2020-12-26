from django.db import models
# import user
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, null= True, on_delete=models.CASCADE)
    name = models.CharField(max_length=199, null=True)
    email = models.CharField(max_length=199, null=True)
    phone = models.CharField(max_length=199, null=True)
    date_created = models.DateField(auto_now_add=True, null= True)

    def __str__(self):
            return self.name

class Tag(models.Model):
    name = models.CharField(max_length=199, null=True)

    def __str__(self):
            return self.name

class Blog(models.Model):
    CATEGORY = (
        ('Sports', 'Sports'),
        ('Travel', 'Travel'),
        ('Food', 'Food'),
    )
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=10, null=True, choices=CATEGORY)
    body_text = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
            return "%s %s" % (self.title, self.author.name)
