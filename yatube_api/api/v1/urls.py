from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(
    r'posts',
    views.PostViewSet
)
router.register(
    r'groups',
    views.GroupViewSet
)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    views.CommentViewSet,
    basename='post_comment'
)
router.register(
    r'follow',
    views.FollowViewSet,
    basename='follow'
)

urlpatterns = [
    path('', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
