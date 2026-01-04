from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import PracticeArea, Experience, Credential, Philosophy
from .serializers import (
    PracticeAreaSerializer,
    ExperienceSerializer,
    CredentialSerializer,
    PhilosophySerializer
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
