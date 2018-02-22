from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):

    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):

    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=70)#store title
    body = models.TextField()#store content

    created_time = models.DateTimeField()#store create time
    modified_time = models.DateTimeField()#store modified time

    abstract = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)


    author = models.ForeignKey(User)#django has written for us as django.contrib.auth.models

    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})


    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])