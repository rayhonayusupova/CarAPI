from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView
)


router=DefaultRouter()
router.register('cars',views.CarViewSet)

urlpatterns=[
    path('api/',include(router.urls), name='cars'),
    path('admin/', admin.site.urls),
    path('', include('cars.urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),
]