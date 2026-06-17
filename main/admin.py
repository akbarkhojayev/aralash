from tokenize import Comment

from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(BlogPost)
admin.site.register(Club)
admin.site.register(Player)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Notebook)