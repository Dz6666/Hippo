# _*_coding : UTF-8_*_
# 开发人员 : daizhe
# 开发时间 : 2021/2/17 13:04
from django.urls import path,include,re_path
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
urlpatterns = [
    re_path(r'^login/', obtain_jwt_token),

    # path('verify/', verify_jwt_token), #这是只是校验token有效性
    # path(r'verify_and_refresh/', refresh_jwt_token), #校验并生成新的token
    path(r'^verify/', refresh_jwt_token),   # refresh_jwt_token 校验token有效性，并且刷新token
]

