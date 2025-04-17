from django.contrib import admin

# Register your models here.
from .models import lawyer,case,client,category,User

# admin.site.register(lawyer)
# admin.site.register(case)
# admin.site.register(client)
# admin.site.register(category)
admin.site.register(User)
