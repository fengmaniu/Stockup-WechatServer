from django.db import models
from dynamic_scraper.models import Scraper, SchedulerRuntime
from scrapy_djangoitem import DjangoItem
# Create your models here.
class User_basic(models.Model):
	user_name = models.CharField(max_length=200)
	user_stockcode = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')

class User_information(models.Model):
	user = models.ForeignKey(User_basic, on_delete=models.CASCADE)
	user_portrait = models.CharField(max_length=200)
	user_gender = models.CharField(max_length=200)
	user_address = models.CharField(max_length=200)
	user_wechatnum = models.CharField(max_length=200)

class stock_information(models.Model):
	user = models.ForeignKey(User_basic, on_delete=models.CASCADE)
	stock_name = models.CharField(max_length=200)
	stock_amount = models.CharField(max_length=200)
	stockvalue_daily = models.CharField(max_length=200)
	date_whenbuy = models.DateTimeField('date buy stock')

class news_collection(models.Model):
	user = models.ForeignKey(User_basic, on_delete=models.CASCADE)
	newscollection_url = models.CharField(max_length=200)
	newscollection_pic = models.CharField(max_length=200)

class news_personal(models.Model):
	user = models.ForeignKey(User_basic, on_delete=models.CASCADE)
	newspersonal_url = models.CharField(max_length=200)
	newspersonal_pic = models.CharField(max_length=200)

# add = User_basic(user_name='wahaha',user_stockcode='hahawa' )
# add.save() #不save无法保存到数据库
a = User_basic.objects.get(user_name='czg')