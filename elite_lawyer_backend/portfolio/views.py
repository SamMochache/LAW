from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import PracticeArea, Experience, Credential, Philosophy, ContactInquiry, Achievement, Testimonial, Recognition
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import status
from .serializers import (
    PracticeAreaSerializer,
    ExperienceSerializer,
    CredentialSerializer,
    PhilosophySerializer,
    ContactInquirySerializer,
    AchievementSerializer,      
    TestimonialSerializer,
    RecognitionSerializer
)


class PracticeAreaList(APIView):
    def get(self, request):
        data = PracticeAreaSerializer(
            PracticeArea.objects.all(), many=True
        ).data
        return Response(data)


class ExperienceList(APIView):
    def get(self, request):
        data = ExperienceSerializer(
            Experience.objects.all(), many=True
        ).data
        return Response(data)


class CredentialList(APIView):
    def get(self, request):
        data = CredentialSerializer(
            Credential.objects.all(), many=True
        ).data
        return Response(data)


class PhilosophyView(APIView):
    def get(self, request):
        philosophy = Philosophy.objects.first()
        if not philosophy:
            return Response({})
        return Response(
            PhilosophySerializer(philosophy).data
        )


# NEW VIEWS FOR CONTACT FORM
class ContactInquiryView(APIView):
    """
    Handle contact form submissions
    POST: Create new inquiry and send email notification
    """
    def post(self, request):
        serializer = ContactInquirySerializer(data=request.data)
        
        if serializer.is_valid():
            # Save the inquiry
            inquiry = serializer.save()
            
            # Prepare email content
            email_subject = f'New Consultation Request - {inquiry.get_matter_type_display()}'
            email_body = f"""
New Consultation Request Received

Client Information:
-------------------
Name: {inquiry.full_name}
Company: {inquiry.company or 'N/A'}
Email: {inquiry.email}
Phone: {inquiry.phone}

Matter Details:
--------------
Type: {inquiry.get_matter_type_display()}
Urgency: {inquiry.get_urgency_display()}
Referral Source: {inquiry.referral_source or 'Not specified'}

Description:
{inquiry.details}

-------------------
Submitted: {inquiry.submitted_at.strftime('%B %d, %Y at %I:%M %p')}
Inquiry ID: {inquiry.id}

To review and respond, login to the admin panel:
{request.build_absolute_uri('/admin/portfolio/contactinquiry/')}
            """
            
            # Send email notification
            try:
                send_mail(
                    subject=email_subject,
                    message=email_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['sammochache01@gmail.com'],  # Change this to your email
                    fail_silently=False,
                )
            except Exception as e:
                # Log error but don't fail the request
                print(f"Email sending failed: {str(e)}")
            
            return Response(
                {
                    'message': 'Your inquiry has been received and will be reviewed within 24 hours.',
                    'inquiry_id': inquiry.id
                },
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# NEW VIEWS FOR TRUST SIGNALS
class AchievementList(APIView):
    """
    GET: List all achievement metrics
    """
    def get(self, request):
        achievements = Achievement.objects.all()
        serializer = AchievementSerializer(achievements, many=True)
        return Response(serializer.data)


class TestimonialList(APIView):
    """
    GET: List active testimonials
    """
    def get(self, request):
        testimonials = Testimonial.objects.filter(is_active=True)
        serializer = TestimonialSerializer(testimonials, many=True)
        return Response(serializer.data)


class RecognitionList(APIView):
    """
    GET: List active professional recognitions
    """
    def get(self, request):
        recognitions = Recognition.objects.filter(is_active=True)
        serializer = RecognitionSerializer(recognitions, many=True)
        return Response(serializer.data)


class TrustSignalsView(APIView):
    """
    GET: Return all trust signal data in one request (optimized)
    """
    def get(self, request):
        achievements = Achievement.objects.all()
        testimonials = Testimonial.objects.filter(is_active=True)
        recognitions = Recognition.objects.filter(is_active=True)
        
        return Response({
            'achievements': AchievementSerializer(achievements, many=True).data,
            'testimonials': TestimonialSerializer(testimonials, many=True).data,
            'recognitions': RecognitionSerializer(recognitions, many=True).data,
        })