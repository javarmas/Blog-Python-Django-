from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse  # Reverse allows to reference an object by its URL template name

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):  # You should add __str__() and get_absolute_url() method to each model you write.
        return self.title

    def get_absolute_url(self):  # It sets a canonical URL for an object so even if the structure of your URLs changes,
        # the reference to the specified object is the same.
        return reverse('post_detail', args=[str(self.id)])  # Allows to reference post_detail. So we’re telling Django
        # that the ultimate location of a Post entry is its post_detail view which is posts/<int:pk>/ (This means, after
        # creating a post, the page will redirect you to the specific template of the post created).

