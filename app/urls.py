from django.urls import path, include
from .views import Generic, GenericViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('genericviewset', GenericViewset, basename='genericviewset')

urlpatterns = [
    path('genericviewset/',include(router.urls)),
    path('generic/', Generic.as_view()),
    path('generic/<int:id>/', Generic.as_view()),
]
