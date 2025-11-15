from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('company.urls')),
    path('api/', include('collaborator.urls')),
    path('api/', include('article.urls')),
    path('api/', include('category.urls')),
    path('api/', include('application.urls'))
]