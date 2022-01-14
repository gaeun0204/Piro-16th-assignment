from django.db import models

class Review(models.Model):
	title = model.CharField(verbose_name='����', max_length=50)
    director = models.CharField(verbose_name='����', max_length=20)
    actor = models.CharField(verbose_name='�ֿ�', max_length=50)
	genre = models.CharField(verbose_name='�帣', max_length=20)
	rating  = models.FloatField(verbose_name='����')
    runningTime = models.DurationField(verbose_name='����Ÿ��')
    content = models.TextField(verbose_name='���䳻��')

	def __str__(self):
		return self.title