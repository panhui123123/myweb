from django.db import models

# Create your models here.


class UserInfo(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=10)
    phone = models.IntegerField(verbose_name='电话')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name






