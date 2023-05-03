from django.contrib import admin
from django.contrib.auth.models import Group


admin.site.site_header = 'Deepak_sahani_7738'
admin.site.site_title = 'Deepak Sahani'
admin.site.index_title = 'Django projects'

       
admin.site.unregister(Group)

