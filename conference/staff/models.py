from __future__ import unicode_literals
from django.db import models

class equipment(models.Model):
    s = [
        ("已完成", "已完成"),
        ("待完成", "待完成")
    ]
    fome_id = models.AutoField(primary_key=True) #设置AutoField，不要加default属性
    room = models.CharField(max_length = 128)
    user_id = models.CharField(max_length = 128)
    service = models.CharField(max_length = 128)
    data = models.DateTimeField(auto_now_add=True,)
    equip = models.CharField(max_length = 128)
    state =models.CharField(max_length = 128,choices=s,default="待完成")
    def __str__(self):
        return str(self.user_id)+"报修了"+str(self.room)
    class Meta:
        db_table = 'Equipment'


        
