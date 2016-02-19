from django.db import models

class User_AGENTIS(models.Model):
	who = models.IntegerField(default=0)
	login = models.CharField(max_length=30)
	surname = models.CharField(max_length=30)
	forename = models.CharField(max_length=30)
	partronyname = models.CharField(max_length=30)
	region = models.IntegerField(default=0)
	email = models.CharField(max_length=30)
	number = models.IntegerField(default=0)
	message = models.CharField(max_length=3000)
	prof = models.CharField(max_length=30)
	
class orders_data(models.Model):
	user_m = models.ForeignKey(User_AGENTIS)
	name_mess = models.CharField(max_length=100)
	sum_mess = models.IntegerField(default=0)
	message = models.CharField(max_length=3000)