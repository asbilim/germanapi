# vocabulary/urls.py

from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ProfessionViewSet, CountryViewSet

# Create a router instance
router = SimpleRouter()

# Register the viewsets
router.register(r'professions', ProfessionViewSet, basename='profession')
router.register(r'countries', CountryViewSet, basename='country')

# URL patterns
urlpatterns = [
    path('vocabulary/', include(router.urls)),
]