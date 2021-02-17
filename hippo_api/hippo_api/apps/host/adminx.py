# _*_coding : UTF-8_*_
# 开发人员 : daizhe
# 开发时间 : 2021/2/17 12:34
import xadmin
from . import models

class HostXadmin(object):
    # list_display = ['id', 'btitle', 'bread', 'bcomment']
    pass

xadmin.site.register(models.Host, HostXadmin)