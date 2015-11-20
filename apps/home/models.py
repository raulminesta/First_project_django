from django.db import models
class User(models.Model):
	name_text=models.TextField(max_length=200)
	hobby_text=models.TextField(max_length=200)
	language_text=models.TextField(max_length=200)
	pub_date=models.DateTimeField('date published')
	class Meta:
		db_table = 'users'
