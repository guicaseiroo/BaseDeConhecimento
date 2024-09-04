from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('', include('conhecimento.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] 
