from django.db import models

# Create your models here.
from django.db import models


class PracticeArea(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = "Practice Area"
        verbose_name_plural = "Practice Areas"
        ordering = ['id']

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()

    class Meta:
        verbose_name = "Selected Experience"
        verbose_name_plural = "Selected Experience"
        ordering = ['id']

    def __str__(self):
        return self.title


class Credential(models.Model):
    title = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    year = models.CharField(max_length=10, blank=True)

    class Meta:
        ordering = ['-year']

    def __str__(self):
        return self.title


class Philosophy(models.Model):
    body = models.TextField()

    def __str__(self):
        return "Legal Philosophy"


# NEW MODELS FOR CONTACT FORM
class ContactInquiry(models.Model):
    MATTER_TYPE_CHOICES = [
        ('corporate', 'Corporate & Commercial'),
        ('litigation', 'Commercial Litigation'),
        ('tax', 'Tax Advisory'),
        ('real-estate', 'Real Estate & Property'),
        ('employment', 'Employment Law'),
        ('intellectual', 'Intellectual Property'),
        ('regulatory', 'Regulatory Compliance'),
        ('other', 'Other'),
    ]
    
    URGENCY_CHOICES = [
        ('standard', 'Standard (1-2 weeks)'),
        ('priority', 'Priority (3-5 days)'),
        ('urgent', 'Urgent (24-48 hours)'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending Review'),
        ('reviewing', 'Under Review'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
        ('contacted', 'Client Contacted'),
    ]
    
    # Form fields
    full_name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    matter_type = models.CharField(max_length=50, choices=MATTER_TYPE_CHOICES)
    urgency = models.CharField(max_length=20, choices=URGENCY_CHOICES, default='standard')
    details = models.TextField()
    referral_source = models.CharField(max_length=255, blank=True)
    
    # Admin fields
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    admin_notes = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Contact Inquiry'
        verbose_name_plural = 'Contact Inquiries'
    
    def __str__(self):
        return f"{self.full_name} - {self.matter_type} ({self.status})"


# NEW MODELS FOR TRUST SIGNALS
class Achievement(models.Model):
    metric = models.CharField(max_length=20, help_text="e.g., '30+', '$2B+', '98%'")
    label = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField(default=0, help_text="Display order")
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Achievement Metric'
        verbose_name_plural = 'Achievement Metrics'
    
    def __str__(self):
        return f"{self.metric} - {self.label}"


class Testimonial(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=255, help_text="e.g., 'CEO, Leading Financial Institution'")
    role = models.CharField(max_length=255, help_text="Matter type or industry")
    order = models.IntegerField(default=0, help_text="Display order")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Client Testimonial'
        verbose_name_plural = 'Client Testimonials'
    
    def __str__(self):
        return f"{self.author} - {self.role}"


class Recognition(models.Model):
    title = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    year = models.CharField(max_length=10, blank=True)
    order = models.IntegerField(default=0, help_text="Display order")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order', '-year']
        verbose_name = 'Professional Recognition'
        verbose_name_plural = 'Professional Recognition'
    
    def __str__(self):
        return self.title