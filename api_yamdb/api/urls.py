from rest_framework.routers import DefaultRouter
from django.urls import include, path

app_name = 'api'

router_v1 = DefaultRouter()

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
