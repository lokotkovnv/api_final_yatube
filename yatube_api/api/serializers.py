from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Post, Group, Follow, User


SELFFOLLOWERROR = 'Вы не можете подписаться на самого себя.'
UNIQUEFOLLOWERROR = 'Вы уже подписаны на этого пользователя.'


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.StringRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault(),
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault(),
    )

    def validate(self, data):
        user = data['user']
        following = data['following']

        if user == following:
            raise serializers.ValidationError(
                (SELFFOLLOWERROR)
            )

        return data

    class Meta:
        model = Follow
        fields = ('user', 'following')
        validators = (
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message=UNIQUEFOLLOWERROR
            ),
        )


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, required=False)
    author = serializers.StringRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = (
            'id', 'text', 'pub_date', 'author', 'image', 'group', 'comments'
        )
