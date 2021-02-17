# _*_coding : UTF-8_*_
# 开发人员 : daizhe
# 开发时间 : 2021/2/17 13:04
from django.urls import path,include,re_path
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    re_path(r'^login/', obtain_jwt_token),
]

