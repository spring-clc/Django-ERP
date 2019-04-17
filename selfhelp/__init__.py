#coding:utf-8
from django.apps import AppConfig
import os

default_app_config = "selfhelp.MyAppConfig"

def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]

class MyAppConfig(AppConfig):
    name= get_current_app_name(__file__)
    verbose_name = '个人自助'