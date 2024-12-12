from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet, UserViewSet, LoginView
 
router = DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contact')
 
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/auth/register/', UserViewSet.as_view({'post': 'register'}), name='register'),
    path('api/auth/login/', LoginView.as_view(), name='login'),
]