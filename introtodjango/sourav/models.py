# we just creating all the database models here .. meaning database name and what will be the attributes

from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # we will show the title in the article in admin dashboard
    def __str__(self):
        return self.title

    # changing the model name article to blog posts
    class Meta:
        verbose_name_plural = "Blog posts"
