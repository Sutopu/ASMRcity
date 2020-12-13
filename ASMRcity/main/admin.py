from django.contrib import admin
from main.models import AsmrVideo, AsmrCreator, AsmrCategory, UserVideoListEntry

admin.site.register(AsmrVideo)
# Register your models here.
admin.site.register(AsmrCreator)
admin.site.register(AsmrCategory)
admin.site.register(UserVideoListEntry)