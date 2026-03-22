from django.contrib import admin
from .models import Movie, Category, Tag, Actor, Director

# Register your models here.
admin.site.register(Movie)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Actor)
admin.site.register(Director)
