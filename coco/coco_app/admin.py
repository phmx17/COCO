from django.contrib import admin

from .models import Time, Project

# Register your models here.
class TimesAdmin(admin.ModelAdmin):
    # readonly_fields = ('developer',)  # tuple
    list_filter = ('developer', 'date')  # filter in right panel
    list_display = ('date', 'developer', 'project', 'time')  # show cols

class ProjectsAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    list_display = ('title', 'short_cut')

'''Don't forget to register !!'''
admin.site.register(Time, TimesAdmin)
admin.site.register(Project, ProjectsAdmin)
