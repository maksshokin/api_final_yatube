from rest_framework import serializers

from posts.models import Comment, Group, Post, User, Follow


class PostSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Group.objects.all(),
        required=False
    )
    comment = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Comment.objects.all(),
        required=False
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = (
            'id',
            'text',
            'author',
            'image',
            'pub_date',
            'group',
            'comment',
        )
        read_only_fields = ('author',)
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'description',
            'title',
            'slug',
        )
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = (
            'id',
            'text',
            'author',
            'created',
            'post',
        )
        read_only_fields = ('author',)
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields =('user', 'following')
