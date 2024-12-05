from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from api.views import CommentViewSet, FollowViewSet, PostViewSet, GroupViewSet

v1_router = routers.DefaultRouter()
v1_router.register('v1/posts', PostViewSet)
v1_router.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments')
v1_router.register('v1/groups', GroupViewSet)
v1_router.register(r'v1/follow', FollowViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('', include(v1_router.urls)),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )