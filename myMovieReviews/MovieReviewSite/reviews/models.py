from django.db import models

class Review(models.Model):
	title = model.CharField(verbose_name='제목', max_length=50)
    director = models.CharField(verbose_name='감독', max_length=20)
    actor = models.CharField(verbose_name='주연', max_length=50)
	genre = models.CharField(verbose_name='장르', max_length=20)
	rating  = models.FloatField(verbose_name='별점')
    runningTime = models.DurationField(verbose_name='러닝타임')
    content = models.TextField(verbose_name='리뷰내용')

	def __str__(self):
		return self.title