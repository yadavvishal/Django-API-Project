from rest_framework import serializers
from .models import CustomUser, Paragraph


class UserSerializer(serializers.ModelSerializer):
    createdAt = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    modifiedAt = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'dob', 'createdAt', 'modifiedAt']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            dob=validated_data.get('dob')
        )
        return user


class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['id', 'content']
