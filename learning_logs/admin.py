from django.contrib import admin

# Register your models here.
from django.contrib import admin
#在这注册你的模型
from learning_logs.models import Topic
from learning_logs.models import Topic,Entry

admin.site.register(Topic)
admin.site.register(Entry)