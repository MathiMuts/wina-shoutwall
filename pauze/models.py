from django.db import models

class PauzeContent(models.Model):
    title = models.CharField(max_length=200, default="Wina Pauze")
    subtitle = models.CharField(max_length=255, default="Subtitle")
    content = models.TextField(default="Content")
    
    last_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @classmethod
    def get_singleton(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj