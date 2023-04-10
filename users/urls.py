from django.urls import path

from .views import (
					LoginAPIView,
					LogoutAPIView,
					GetDataAPIView,
					)

urlpatterns = [
	path("login", LoginAPIView.as_view(), name="login"),
	path("getData", GetDataAPIView.as_view(), name="get-data"),
	path("logout", LogoutAPIView.as_view(), name="logout"),
]
