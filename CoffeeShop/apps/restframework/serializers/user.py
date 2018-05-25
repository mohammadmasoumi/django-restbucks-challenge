from rest_framework import serializers
from ..models.user import MyUser
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    """
        Serialize MyUser Model into JSON field
    """

    class Meta(object):
        model = MyUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = MyUser(
            email=validated_data['email'],
            first_name=validated_data['email'],
            last_name=validated_data['email'],
            date_of_birth=validated_data['date_of_birth'],
        )
        user.set_password(make_password(validated_data['password']))
        user.save()
        return user



