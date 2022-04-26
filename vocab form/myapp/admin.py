from django.contrib import admin
from myapp.models import Vocab
# Register your models here.

@admin.register(Vocab)
class vocabadmin(admin.ModelAdmin):
    list_display=['id','uname','word','meaning']
