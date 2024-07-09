from django.contrib import admin
from icoderApp.models import Contact,about,home,container

# Register your models here.

class homeAdmin(admin.ModelAdmin):
    list_display=("Title","sub_title","button1","button2","button3","image")
admin.site.register(home,homeAdmin)

class containerAdmin(admin.ModelAdmin):
    list_display=("name","title","date","detail","image")
admin.site.register(container,containerAdmin)

admin.site.register(Contact)


class AboutAdmin(admin.ModelAdmin):
    list_display=("title","subtitle","description","image",)
admin.site.register(about,AboutAdmin)
