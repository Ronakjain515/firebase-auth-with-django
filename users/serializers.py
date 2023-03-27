from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
	"""
	Serializer class for login users.
	"""
	email = serializers.EmailField(allow_null=False, allow_blank=False, required=True)
	password = serializers.CharField(allow_null=False, allow_blank=False, required=True)
