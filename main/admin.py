from django.contrib import admin
# from .models import *

from .models import Cinema
from .models import Movie
from .models import Review
from .models import Genre
# Register your models here.
admin.site.register(Cinema)
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Genre)
