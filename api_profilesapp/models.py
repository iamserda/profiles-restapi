from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Modeling the UserProfile table in the db"""
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64, default=None)
    last_name = models.CharField(max_length=255, default=None)
    email = models.EmailField(max_length=255, unique=True) #unique because it is the username.
    password = models.CharField(max_length=255, default=None)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    # here we are using the user's email as the username for the app.
    USERNAME_FIELD = 'email' #main required field, app requires a username. 
    REQUIRED_FIELDS = ['first_name', 'last_name'] # other required field.
    
    
    def get_full_name(self):
        """ returns a dictionary containing the user's first, middle(if any), last as full name """
        full_name = {
            'first': self.first_name,
            'middle': self.middle_name,
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

class UserProfileManager(BaseUserManager):
    """ instances of this class are used by the Django CLI to create new users"""
    
    def create_user(self, email, first, last, middle=None, password=None):
        """ method used to create new users with standard or non-admin privileges."""
        try:
            if not email:
                raise ValueError("In order to create an account, a new user MUST have an email address!")
            
            self.email = self.normalize_email(email)
            user = self.model(email=email, first_name=first, last_name=last, middle_name=middle)
            user.set_password(password)
            user.save(using=self._db)
            return user
        
        except Exception as re:
            print(re)
            print("No new profile was created. No changes were made to the database. Please try again")
            return None

    def create_superuser(self, email, first, last, password, middle=None):
        """a method used to create new user objects with admin privileges. """
        try:
            user = self.create_user(email, first, last,middle, password)
            if not user:
                raise ValueError("Couldn't create a new admin account.\nPlease check your inputs and try again!")
            user.is_superusesr = True if user else False
            user.is_staff = True if user.is_superuser else False
            user.save(using=self._db)
            return user
        
        except Exception as re:
            print(re)
            print("Could not creaete a new administrator.")
            return None