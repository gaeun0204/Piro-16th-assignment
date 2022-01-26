from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	like = models.IntegerField(default=0)

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
	comment = models.TextField()