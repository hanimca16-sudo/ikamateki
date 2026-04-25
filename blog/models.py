from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    RESIDENCE_CHOICES = [
        ('1',       'إقامة 1'),
        ('2',       'إقامة 2'),
        ('3',       'إقامة 3'),
        ('outside', 'خارج الإقامة'),
    ]
    author     = models.ForeignKey(User, on_delete=models.CASCADE)
    content    = models.TextField()
    image      = models.ImageField(upload_to='posts/', blank=True)
    residence  = models.CharField(max_length=10, choices=RESIDENCE_CHOICES, default='1')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.created_at}'

class Comment(models.Model):
    post       = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author     = models.ForeignKey(User, on_delete=models.CASCADE)
    content    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.post}'

class Message(models.Model):
    sender     = models.ForeignKey(User, related_name='sent', on_delete=models.CASCADE)
    receiver   = models.ForeignKey(User, related_name='received', on_delete=models.CASCADE)
    content    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} -> {self.receiver}'