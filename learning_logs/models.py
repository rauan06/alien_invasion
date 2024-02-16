from django.db import models

class Topic(models.Model):
    """A topic that user is learning about."""
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """Returning string representation of the model."""
        return self.text

class Entry(models.Model):
    """User notes about the topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return string representation of the model."""
        return self.text[:50] + "..."