# _*_coding : UTF-8_*_
# 开发人员 : daizhe
# 开发时间 : 2021/2/17 12:30
# _*_coding : UTF-8_*_
# 开发人员 : daizhe
# 开发时间 : 2021/1/23 17:54
import xadmin
from xadmin import views

class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True # 引导控制盘(其实就是我们的左侧菜单栏)

xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "运维平台管理"  # 设置站点标题
    site_footer = "Opstrator有限公司"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠rdion"  # 设置菜单折叠

xadmin.site.register(views.CommAdminView, GlobalSettings)