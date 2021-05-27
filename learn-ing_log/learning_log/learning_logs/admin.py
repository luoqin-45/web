# from learning_log.learning_logs.models import Entry
from django.contrib import admin

# Register your models here.
from learning_logs.models import Topic,Entry
admin.site.register(Topic)
admin.site.register(Entry)