from django.contrib import admin

from reviews.models import Design, Review, Step, Process, ProcessStep

admin.site.register(Design)
admin.site.register(Review)
admin.site.register(Step)
admin.site.register(Process)
admin.site.register(ProcessStep)
