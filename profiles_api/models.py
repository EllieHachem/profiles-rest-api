from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager



# Create your models here.
class UserProfileManager(BaserUserManager):
    """Manager for user profiles"""
    def create_user(self,email,name,password=none):
        """Create a new user profile"""
        #if we an email address has been provided
        if not email:
            raise ValueError("Users must have an email address")
            #normalizing an email address
        email = self.normalize_email(email)
        #create new model that user manager representing
        user = self.model(email=email,name=name)
        #storing password as a hash not as plain text using this method
        user.set_password(password)
        #saving user model
        user.save(using=self._db)
        return user

     #creating super user to be admin + to use the create user function
     #here password is not null since we need to have access
    def create_superuser(self,email,name,password):
        """Create and save new superuser with given details"""
        #use the create_function to create a user  
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db
        return user


#creating user profile model
class UserProfile(AbstractBaseUser,PermissionsMixin): #inherited the 2 base classes
    """Database modle for users profile"""
    email = models.EmailFields(max_length=255, unique=true)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(defualt=True)
    is_staff = models.BooleanField(default=False)


objects = UserProfileManager()


USERNAME_FIELD = 'email'
REQUIRED_FIELDS = ['name']


def get_full_name(self):
    """retrive full name of user"""
    return.self.name

def get_short_name(self):
    """retrive short name of user"""
    return.self.name

def __str__(self):
    """return string represenation of our user"""
    return self.email
