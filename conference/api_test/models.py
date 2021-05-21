# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Conference(models.Model):
    conference_id = models.CharField(max_length = 128,verbose_name = "编号",unique = True)
    conference_capacity = models.IntegerField(verbose_name = "容量")
    conference_authorization = models.IntegerField(verbose_name = "权限")
    conference_status = models.IntegerField(verbose_name = "状态")
    conference_createtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    conference_updatetime = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    class Meta:
        db_table = 'conference'
    def __str__(self):
        return self.conference_id


