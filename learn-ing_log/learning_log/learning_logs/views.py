from typing import ContextManager
from .models import Topic,Entry
from django.shortcuts import render

# Create your views here.
def index(request):
    """学习笔记的主页"""
    return render(request, "index.html")

def topics(request):
    #显示所有主题
    topics = Topic.objects.order_by("date_added")
    context = {'topics':topics}
    return render(request,'topics.html',context)

def topic(request, topic_id):
    #显示单个主题及其所有的条目
    topic = Topic.objects.get(id=topic_id)
    entries =topic.entry_set.order_by('-date_added')
    context = {'topic':topic,"entries":entries}
    return render(request, 'topic.html',context)