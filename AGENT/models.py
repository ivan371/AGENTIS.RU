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
	img = models.ImageField(default=0, upload_to='user_media')
	
class orders_data(models.Model):
	user_m = models.ForeignKey(User_AGENTIS)
	name_mess = models.CharField(max_length=100)
	sum_mess = models.IntegerField(default=0)
	message = models.CharField(max_length=3000)

class order(models.Model):
	order_from = models.ForeignKey(User_AGENTIS, related_name='order_from')
	order_to = models.ForeignKey(User_AGENTIS, related_name='order_to')
	href_order = models.CharField(default=0, max_length=100)
	status = models.IntegerField(default=0)

class message(models.Model):
	mess_from = models.ForeignKey(User_AGENTIS, related_name='mess_from')
	mess_to = models.ForeignKey(User_AGENTIS, related_name='mess_to')
	status = models.IntegerField(default=0)
	message = models.CharField(max_length=3000)
	author = models.IntegerField(default=0)


	
