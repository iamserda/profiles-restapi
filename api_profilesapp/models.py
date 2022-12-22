from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """ instances of this class are used by the Django CLI to create new users"""

    def create_user(self, email, first_name, last_name, password=None):
        """ method used to create new users with standard or non-admin privileges."""
        try:
            if not email:
                raise ValueError(
                    "In order to create an account, a new user MUST have an email address!")
            if not first_name:
                raise ValueError("A First name is required!")

            self.email = self.normalize_email(email)
            user = self.model(email=email, first_name=first_name,
                              last_name=last_name)

            if password:
                user.set_password(password)

            user.save(using=self._db)
            print('Created new user!')
            return user

        except Exception as re:
            print(re)
            print(
                "FAILED: No new profile was created. No changes were made to the database. Please try again")
            return None

    def create_superuser(self, email, first_name, last_name, password):
        """a method used to create new user objects with admin privileges. """
        try:
            if not password:
                raise ValueError(
                    "In order to create an staff account, a password is REQUIRED!")

            user = self.create_user(
                email, first_name, last_name, password)

            if not user:
                raise ValueError(
                    """Couldn't create a new admin account.\nPlease check your inputs and try again!""")

            user.is_superuser = True
            user.is_staff = True
            user.save(using=self._db)
            print("Created new superuser: ", user.is_superuser)
            return user

        except Exception as re:
            print(re)
            print("FAILED: Could not creaete a new super user.")
            return None


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Modeling the UserProfile table in the db"""
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=255)
    # unique because it is the username.
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    # here we are using the user's email as the username for the app.
    USERNAME_FIELD = 'email'  # main required field, app requires a username.
    REQUIRED_FIELDS = ['first_name', 'last_name']  # other required field.

    def get_full_name(self):
        """ returns a dictionary containing the user's first, last as full name """
        full_name = {
            'first': self.first_name,
            'last': self.last_name,
        }
        return full_name

    def get_short_name(self):
        """ returns a dictionary containing the user's first, last"""
        short_name = {
            'first': self.first_name,
            'last': self.last_name,
        }
        return short_name

    def __str__(self):
        return self.email
