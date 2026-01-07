from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import PracticeArea, Experience, Credential, Philosophy, ContactInquiry, Achievement, Testimonial, Recognition


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


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 
        'email', 
        'matter_type', 
        'urgency', 
        'status',
        'submitted_at'
    )
    list_filter = ('status', 'matter_type', 'urgency', 'submitted_at')
    search_fields = ('full_name', 'email', 'company', 'details')
    readonly_fields = ('submitted_at',)
    
    fieldsets = (
        ('Client Information', {
            'fields': ('full_name', 'company', 'email', 'phone')
        }),
        ('Matter Details', {
            'fields': ('matter_type', 'urgency', 'details', 'referral_source')
        }),
        ('Status & Review', {
            'fields': ('status', 'admin_notes', 'reviewed_at', 'submitted_at')
        }),
    )
    
    actions = ['mark_as_reviewing', 'mark_as_accepted', 'mark_as_contacted']
    
    def mark_as_reviewing(self, request, queryset):
        queryset.update(status='reviewing')
    mark_as_reviewing.short_description = "Mark as Under Review"
    
    def mark_as_accepted(self, request, queryset):
        queryset.update(status='accepted')
    mark_as_accepted.short_description = "Mark as Accepted"
    
    def mark_as_contacted(self, request, queryset):
        queryset.update(status='contacted')
    mark_as_contacted.short_description = "Mark as Contacted"


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('metric', 'label', 'order')
    list_editable = ('order',)
    ordering = ('order',)
    
    fieldsets = (
        (None, {
            'fields': ('metric', 'label', 'description', 'order'),
            'description': 'Create achievement metrics to display in the Trust Signals section.'
        }),
    )


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author', 'role', 'order', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('order', 'is_active')
    search_fields = ('author', 'quote')
    ordering = ('order',)
    
    fieldsets = (
        (None, {
            'fields': ('quote', 'author', 'role'),
            'description': 'Add client testimonials. Keep author attribution professional but anonymous (e.g., "CEO, Leading Financial Institution").'
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )


@admin.register(Recognition)
class RecognitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'year', 'order', 'is_active')
    list_filter = ('is_active', 'year')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'organization')
    ordering = ('order', '-year')
    
    fieldsets = (
        (None, {
            'fields': ('title', 'organization', 'year'),
            'description': 'Add professional recognitions, awards, and accolades.'
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )