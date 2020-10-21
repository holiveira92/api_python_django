#import from used libraries
from django.contrib import admin
from django.urls import path, include
from core.views import RealtyViewSet, Real_EstateViewSet
from rest_framework import routers

#Registration of the API routes used
router = routers.DefaultRouter()
router.register(r'realty', RealtyViewSet)
router.register(r'real_estate', Real_EstateViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
