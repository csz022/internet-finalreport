from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Member(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    unit = models.CharField(max_length=100)
    birthday = models.DateField()
    bio = models.TextField()
    youtube_id = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return self.name

class MemberMessage(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='message_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} 留言於 {self.member.name}"