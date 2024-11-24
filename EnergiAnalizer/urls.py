








from rest_framework.authtoken import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('users/', include('users.urls')),  
    path('post/', include('post.urls')),  
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),    
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),

]
