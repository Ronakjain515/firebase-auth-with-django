from django.contrib.auth.models import BaseUserManager

from utilities.firebase import create_user


class CustomUserManager(BaseUserManager):
    """
    Class for creating custom manager for managing custom user.
    """
    def create_user(self, email=None, first_name=None, last_name=None, password=None, **extra_fields):
        """
        Function for creating user w.r.t custom user.
        """
        uid = create_user(email, password)

        user = self.model()
        user.uid = uid
        user.first_name = first_name
        user.last_name = last_name
        user.is_superuser = False
        user.is_active = True
        user.is_staff = False
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, email, password, last_name):
        """
        Function for creating superuser.
        """
        user = self.create_user(
            email,
            first_name,
            last_name,
            password,
            role='SUPER_ADMIN',
            status='ACTIVE'
        )
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user
