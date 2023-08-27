from rest_framework import serializers, permissions

from django.contrib.auth.models import User

from events1.models import Event


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    permission_classes = [permissions.IsAuthenticated]

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'meeting_time', 'description', 'users']