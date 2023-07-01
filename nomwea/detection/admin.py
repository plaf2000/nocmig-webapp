from django.contrib import admin
from .models import *
from multidb import MultiDBModelAdmin


class DetectionAdmin(MultiDBModelAdmin):
    using = 'detection'

admin.site.register(Codes, DetectionAdmin)
admin.site.register(NonBird, DetectionAdmin)
admin.site.register(Species, DetectionAdmin)

