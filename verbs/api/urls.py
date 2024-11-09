from django.urls import path,include
from rest_framework.routers import SimpleRouter
from .views import VerbViewSet

router = SimpleRouter()

router.register(r'all', VerbViewSet)

urlpatterns = [
    path('verbs/',include(router.urls))
]
