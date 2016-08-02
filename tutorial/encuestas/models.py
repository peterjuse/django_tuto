import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Poll(models.Model):
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return	self.question

	def fue_recientemente_publicado(self):
		return	self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	
	fue_recientemente_publicado.admin_order_field = 'pub_date'
	fue_recientemente_publicado.boolean = True
	fue_recientemente_publicado.short_description = 'Published recently?'

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __unicode__(self):
		return self.choice_text