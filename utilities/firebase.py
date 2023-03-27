import firebase_admin
import firebase_admin.auth as auth
from firebase_admin import credentials
from rest_framework import authentication

cred = credentials.Certificate("static/fir-auth-with-django-firebase-adminsdk-1zepn-3023fd129c.json")
firebase_admin.initialize_app(cred)


class FirebaseAuthentication(authentication.BaseAuthentication):
	def authenticate(self, request):

		token = request.headers.get('Authorization')
		if not token:
			return None

		try:
			decoded_token = auth.verify_id_token(token)
			uid = decoded_token["uid"]
		except:
			return None

		try:
			user = User.objects.get(username=uid)
			return user

		except ObjectDoesNotExist:
			return None
