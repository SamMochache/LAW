from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def root_view(request):
    return JsonResponse({
        'status': 'success',
        'message': 'Backend is live!',
        'endpoints': {
            'admin': '/admin/',
            'api': '/api/',
            'practice_areas': '/api/practice-areas/',
            'experience': '/api/experience/',
            'credentials': '/api/credentials/',
            'philosophy': '/api/philosophy/',
            'contact': '/api/contact/',
            'trust_signals': '/api/trust-signals/',
        }
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('portfolio.urls')),
    path('', root_view),
]