from django.db import models

# Create your models here.

class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text




class Entry(models.Model):
    """Something specific learning about a topic"""
    """When a topic is deleted - delete all related entries"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    """Meta class allows us to set a special attribute telling
    Django to use Entries when it needs to refer to more than one entry"""
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model"""
        """Django returns the first 50 characters of text so
        that we are not always displaying the full entry"""
        return f"{self.text[:50]}..."