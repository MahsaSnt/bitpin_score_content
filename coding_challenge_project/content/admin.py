from django.contrib import admin

from .models import Score, Content


admin.site.register((Content, Score,))
