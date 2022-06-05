from rest_framework.routers import DefaultRouter
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    UserViewSet, GenreViewSet, CategoryViewSet, TitleViewSet,
    signup, token
)


app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet, basename='users')
router_v1.register(r'categories', CategoryViewSet, basename='categories')
router_v1.register(r'genres', GenreViewSet, basename='genres')
router_v1.register(r'titles', TitleViewSet, basename='titles')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/token/', token, name='token'),
    #path('v1/auth/token/refresh/', TokenRefreshView.as_view(),
    # name='token_refresh'),
    path('v1/auth/signup/', signup, name='signup'),
    #path('v1/users/me/', ),

]
