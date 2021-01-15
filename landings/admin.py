from django.contrib import admin
from .models import Organization, BasicInfo, Detail, Info
# Register your models here.
  
admin.site.register(Organization)
admin.site.register(BasicInfo)
admin.site.register(Detail)
admin.site.register(Info)
