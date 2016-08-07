from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=50)
    version = models.CharField(max_length=30)
    short_description = models.CharField(max_length = 200)
    screenshot_url_1 = models.CharField(max_length = 50)
    screenshot_url_2 = models.CharField(max_length = 50, default="null")
    screenshot_url_3 = models.CharField(max_length = 50, default="null")
    screenshot_url_4 = models.CharField(max_length = 50, default="null")
    screenshot_url_5 = models.CharField(max_length = 50, default="null")
    status = models.CharField(max_length=20)
    source_code_link = models.CharField(max_length=50)
    technologies_used = models.CharField(max_length=300)
    long_description = models.TextField()
    store_logo_url = models.CharField(max_length=50, default="null")
    store_url = models.CharField(max_length=300, default="null")

    def __str__(self):
        return self.title
