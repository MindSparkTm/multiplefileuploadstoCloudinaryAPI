# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django import forms
from .models import Photo


# Register your models here.

class Photoinfo(admin.ModelAdmin):

    list_display = ['created','title','description','publicid','url']

admin.site.register(Photo, Photoinfo)