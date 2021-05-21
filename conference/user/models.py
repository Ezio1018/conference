from django.db import models

# Create your models here.
class User(models.Model):
    gender = [
        ("m", "男"),
        ("f", "女")
    ]
    role=[
        ("user","用户"),
        ("admin","管理员"),
        ("staff","后勤")
    ]
    user_id= models.CharField(max_length=50, verbose_name="id",unique=True)
    name = models.CharField(max_length=50, verbose_name="姓名")
    gender = models.CharField(max_length=10, choices=gender, default='m', verbose_name="性别")
    department = models.CharField(max_length=30, verbose_name="部门",default="技术部")
    email = models.EmailField(unique=True,verbose_name="邮箱")
    password = models.CharField(max_length=30, verbose_name="密码")
    image = models.FileField(blank=True, null=True, upload_to='goods', verbose_name='图片')
    identity=models.CharField(max_length=10, choices=role, default='user', verbose_name="身份")
    level = models.IntegerField(default=0)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s (%s)" % (self.id, self.name)

    class Meta:
            db_table = 'User'
            ordering = ['c_time']
            verbose_name = '用户'
            verbose_name_plural = '用户'
            db_table = 'User'


# class conferance_room(models.Model):
#     pass
