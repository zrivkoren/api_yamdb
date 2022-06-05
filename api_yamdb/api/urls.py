from rest_framework.routers import DefaultRouter
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserViewSet, signup, token


app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/token/', token, name='token'),
    #path('v1/auth/token/refresh/', TokenRefreshView.as_view(),
    # name='token_refresh'),
    path('v1/auth/signup/', signup, name='signup'),
    #path('v1/users/me/', ),

]
