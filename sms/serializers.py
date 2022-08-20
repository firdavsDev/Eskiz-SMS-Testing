from rest_framework import serializers


class ValidatePhoneNumber(serializers.Serializer):
    phone_number = serializers.CharField()