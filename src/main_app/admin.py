from django.contrib import admin

# Register your models here.
from .models import Catalog
from .models import ExampleModel

admin.site.register(Catalog)
admin.site.register(ExampleModel)