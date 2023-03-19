from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserAccountManager(BaseUserManager):
    """Create Account Manager to save user in db"""
    def create_user(self, email, username, password=None):
        """create normal user who is not admin"""
        if not email:
            raise ValueError("User must have an email")
        elif not username:
            raise ValueError("User must have username")
        else:
            user = self.model(
                email=self.normalize_email(email),
                username=username)
            user.set_password(password)
            user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        """create an admin user"""
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password)
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)

        return user


class Account(AbstractBaseUser):
    """'create django custom user model"""
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    """Allow Object manager to be used to save user"""
    objects = UserAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
