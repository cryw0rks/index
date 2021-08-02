from django.contrib import admin
from .models import Project, Service, Banner

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','create_at')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(Project, ProjectAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','create_at')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Service, ServiceAdmin)

class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'status','create_at')
    list_filter = ("status",)
    search_fields = ['title',]
  
admin.site.register(Banner, BannerAdmin)