from django.db import models

class ShoutwallMessage(models.Model):
    poster = models.CharField(max_length=100, help_text="The name of the person posting.")
    content = models.TextField(max_length=1000, help_text="The shoutwall message.")
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.poster} at {self.timestamp.strftime('%Y-%m-%d %H:%M')}"