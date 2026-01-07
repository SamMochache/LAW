from rest_framework import serializers
from .models import PracticeArea, Experience, Credential, Philosophy,ContactInquiry, Achievement, Testimonial, Recognition  


class PracticeAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticeArea
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'


class CredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credential
        fields = '__all__'


class PhilosophySerializer(serializers.ModelSerializer):
    class Meta:
        model = Philosophy
        fields = '__all__'


class ContactInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInquiry
        fields = [
            'id',
            'full_name',
            'company',
            'email',
            'phone',
            'matter_type',
            'urgency',
            'details',
            'referral_source',
            'submitted_at'
        ]
        read_only_fields = ['id', 'submitted_at']
    
    def validate_details(self, value):
        """Ensure details has minimum length"""
        if len(value.strip()) < 100:
            raise serializers.ValidationError(
                "Please provide at least 100 characters describing your matter."
            )
        return value
    
    def validate_email(self, value):
        """Basic email validation"""
        if not value or '@' not in value:
            raise serializers.ValidationError("Please provide a valid email address.")
        return value.lower()
    
    def validate_phone(self, value):
        """Basic phone validation"""
        if not value or len(value.strip()) < 10:
            raise serializers.ValidationError("Please provide a valid phone number.")
        return value

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ['id', 'metric', 'label', 'description']


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id', 'quote', 'author', 'role']


class RecognitionSerializer(serializers.ModelSerializer):
    display_text = serializers.SerializerMethodField()
    
    class Meta:
        model = Recognition
        fields = ['id', 'title', 'organization', 'year', 'display_text']
    
    def get_display_text(self, obj):
        """Combine title and organization for display"""
        if obj.year:
            return f"{obj.title} - {obj.organization} ({obj.year})"
        return f"{obj.title} - {obj.organization}"