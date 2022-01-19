from django.db import models

class Devtool(models.Model):
	name = models.CharField(verbose_name='이름', max_length=20)
	kind = models.CharField(verbose_name='종류', max_length=50)
	description = models.TextField(verbose_name='개발툴설명')

	def __str__(self):
		return self.name

class Idea(models.Model):
	title = models.CharField(verbose_name='아이디어명', max_length=20)
	image = models.ImageField(verbose_name='대표사진', upload_to="image", null=True, blank=True)
	content = models.TextField(verbose_name='아이디어설명')
	interest = models.IntegerField(verbose_name='아이디어관심도')
	# 개발툴 리스트 중에서 항목선택
	devtool = models.ForeignKey(Devtool, on_delete=models.CASCADE, verbose_name='예상개발툴')
	
	def __str__(self):
		return self.title
