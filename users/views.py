from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from .serializers import LoginSerializer
from utilities.utils import ResponseInfo


class LoginAPIView(CreateAPIView):
	"""
	Class for creating api for login user.
	"""
	permission_classes = ()
	authentication_classes = ()
	serializer_class = LoginSerializer

	def __init__(self, **kwargs):
		"""
		 Constructor function for formatting the web response to return.
		"""
		self.response_format = ResponseInfo().response
		super(LoginAPIView, self).__init__(**kwargs)

	def post(self, request, *args, **kwargs):
		"""
		POST Method for login users.
		"""
		return Response(self.response_format)
