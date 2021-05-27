#定义learning_logs的URL模式
from django.urls import path
from django.urls.resolvers import URLPattern 
from . import views
urlpatterns =[
    #主页
    path(r'',views.index, name='index'),
    #显示所有的主题
    path(r'topics/', views.topics, name='topics'),
    path(r'topic/', views.topic, name='topic'),
    path(r'topics/(?P<topic_id>d+)/', views.topic, name='topic'), 
]