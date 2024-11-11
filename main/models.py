from django.db import models
from django.contrib.auth.models import User

class Webpage(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.title

class Session(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True)
    current_webpage = models.ForeignKey(Webpage, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Session {self.code} by {self.host.username}"

class Viewer(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=100)  # Could be device ID or similar
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Viewer {self.identifier} in {self.session.code}"
