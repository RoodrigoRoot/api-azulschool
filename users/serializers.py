from rest_framework import serializers
from django.contrib.auth.models import User


#class UserSerializer(serializers.Serializer):
#    name = serializers.CharField()
#    last_name = serializers.CharField()
#    email = serializers.EmailField()
#    password = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):

    full_name = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email", "password", "full_name")

    def get_full_name(self, obj):
        return "{} {}".format(obj.first_name, obj.last_name)

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get("password"))
        instance.username = validated_data.get("username")
        instance.first_name = validated_data.get("first_name")
        instance.last_name = validated_data.get("last_name")
        instance.email = validated_data.get("email")
        instance.save()
        return instance
