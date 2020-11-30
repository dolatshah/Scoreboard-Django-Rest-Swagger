from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('scoreboardapi.urls')),
   
    path('openapi', get_schema_view(
            title="Scoreboard",
            description="API for backend, handling player interactions",
            version="1.0.0"
        ), name='openapi-schema'),

    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
 ]
