import datetime

from django.db import models
from django.utils import timezone

class Post(models.Model):
    """
    A Blog post.
    Consists of a title, blog text, a publication date and a pinned flag.
    Pinned posts remain at the top.
    """
    title = models.CharField(max_length=100, default='Title')
    text = models.CharField(max_length=5000)
    pub_date = models.DateTimeField('date published')
    pinned = models.BooleanField(default=False)

    def __str__(self):
        """
        Stringify a Post
        """
        return self.title

    def was_published_recently(self):
        """
        Returns True if this post was published recently
        """
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
