from django.contrib import admin
from .models import Project, TechAndTools, Review, Profile
from django.contrib import admin


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','publication_date', )
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    filter_horizontal = ('tech_and_tools',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(TechAndTools)
admin.site.register(Profile)
admin.site.register(Review)


