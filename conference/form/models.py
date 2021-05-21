from __future__ import unicode_literals
from django.db import models

class Form(models.Model):
    room = models.CharField(max_length = 128)
    user_id = models.CharField(max_length = 128)
    data = models.DateTimeField(auto_now_add=True)
    day = models.CharField(max_length = 128)

    time_id = models.IntegerField(blank=True, null=True)
    Participants = models.CharField(max_length = 128)
    statu =  models.CharField(max_length = 128)
    def __str__(self):
        return str(self.user_id)+"预定了"+str(self.room)
    class Meta:
        db_table = 'Form'
        
