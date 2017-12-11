from django.db import models

class Post(models.Model):
    """
    Blog post.
    """
    post_text = models.CharField(max_length=5000)
    pub_date = models.DateTimeField('date published')
