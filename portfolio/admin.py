from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import PracticeArea, Experience, Credential, Philosophy


@admin.register(PracticeArea)
class PracticeAreaAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Credential)
class CredentialAdmin(admin.ModelAdmin):
    list_display = ('title', 'institution', 'year')


@admin.register(Philosophy)
class PhilosophyAdmin(admin.ModelAdmin):
    list_display = ('id',)
