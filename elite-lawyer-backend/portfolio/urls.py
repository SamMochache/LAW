from django.urls import path
from .views import (
    PracticeAreaList,
    ExperienceList,
    CredentialList,
    PhilosophyView
)

urlpatterns = [
    path('practice-areas/', PracticeAreaList.as_view()),
    path('experience/', ExperienceList.as_view()),
    path('credentials/', CredentialList.as_view()),
    path('philosophy/', PhilosophyView.as_view()),
]
