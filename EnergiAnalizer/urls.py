









from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('allauth.urls')),
    path('users/', include('dj_rest_auth.urls')), 
    path('users/registration/', include('dj_rest_auth.registration.urls')),
    path('users/', include('users.urls')),  
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),    
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
