from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
	"""
	Serializer class for login users.
	"""

	email = serializers.EmailField(allow_null=False, allow_blank=False, required=True)

	password = serializers.CharField(allow_null=False, allow_blank=False, required=True)
	default_error_messages = {
		'inactive_account': 'User account is disabled.',
		'invalid_credentials': 'Email address or password is invalid.'
	}

	# def validate(self, attrs):
	# 	"""
	# 	Function for validating and returning the created instance
	# 	based on the validated data of the user.
	# 	"""
	# 	user = login_firebase_user(attrs.pop("email"), attrs.pop('password'))
	# 	print(user)
	# 	if not user.get("error"):
	# 		return attrs
	# 	else:
	# 		raise serializers.ValidationError(self.error_messages['invalid_credentials'])

	def update(self, instance, validated_data):
		pass

	def create(self, validated_data):
		pass
