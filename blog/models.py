from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    date_posted = models.DateField()
    short_description = models.CharField(max_length=500)
    content = models.TextField()
    post_url = models.CharField(max_length=100)

    def __str__(self):
        return self.title
