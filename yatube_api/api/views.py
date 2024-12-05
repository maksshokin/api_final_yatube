from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import pagination
from rest_framework.filters import SearchFilter

from api.permissions import IsAuthor
from api.serializers import CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer, UserSerializer
from posts.models import Follow, Group, Post, User


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthor, permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthor, permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=self.get_post()
        )

    def get_post(self):
        return get_object_or_404(
            Post,
            pk=self.kwargs.get('post_id')
        )

    def get_queryset(self):
        return self.get_post().comments.all()

class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    pagination_class = pagination.LimitOffsetPagination

    filter_backends = (SearchFilter,)
    search_fields = ('following__username', 'user__username',)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer