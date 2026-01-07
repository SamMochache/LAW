from django.urls import path
from .views import (
    PracticeAreaList,
    ExperienceList,
    CredentialList,
    PhilosophyView,
    ContactInquiryView,
    AchievementList,
    TestimonialList,
    RecognitionList,
    TrustSignalsView
)

urlpatterns = [
    path('practice-areas/', PracticeAreaList.as_view()),
    path('experience/', ExperienceList.as_view()),
    path('credentials/', CredentialList.as_view()),
    path('philosophy/', PhilosophyView.as_view()),
    # Contact form
    path('contact/', ContactInquiryView.as_view(), name='contact-inquiry'),
    
    # Trust signals - individual endpoints
    path('achievements/', AchievementList.as_view(), name='achievements'),
    path('testimonials/', TestimonialList.as_view(), name='testimonials'),
    path('recognitions/', RecognitionList.as_view(), name='recognitions'),
    
    # Trust signals - combined endpoint (recommended for better performance)
    path('trust-signals/', TrustSignalsView.as_view(), name='trust-signals'),
]
