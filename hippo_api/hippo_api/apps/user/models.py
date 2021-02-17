from django.db import models
# Create your models here.
from django.contrib.auth.models import  AbstractUser

class User(AbstractUser):
    # 下面就可以扩展字段来使用Django认证系统的用户模型类
    mobile = models.CharField(max_length=15,verbose_name='手机号码')
    # roles = models.ManyToManyField('Role')
    class Meta:
        db_table = 'hippo_user'         # 修改的数据库表前缀
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

