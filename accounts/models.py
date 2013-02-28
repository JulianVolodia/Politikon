# coding: utf-8
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models import F

from constance import config
from fandjango.models import User as FacebookUser


class UserManager(BaseUserManager):
    def return_new_user_object(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username address')

        user = self.model(
            username=UserManager.normalize_email(username),
        )

        user.set_password(password)

        return user

    def create_user(self, username, password=None):
        user = self.return_new_user_object(username)
        user.is_active = True

        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.return_new_user_object(username,
            password=password,
        )
        user.is_admin = True
        user.is_active = True

        user.save(using=self._db)
        return user

    def create_user_with_random_password(self, username, **kwargs):
        user = self.return_new_user_object(username,
            password=None
        )
        password = self.make_random_password()
        user.set_password(password)

        for keyword, argument in kwargs.items():
            setattr(user, keyword, argument)

        user.save(using=self._db)
        return user, password

    def get_for_facebook_user(self, facebook_user):
        user, created = self.get_or_create(username=facebook_user.facebook_id)
        user.facebook_user = facebook_user
        user.save()

        user.topup_cash(amount=config.STARTING_CASH)
        user.save()

        return user


class User(AbstractBaseUser):
    objects = UserManager()

    username = models.CharField(u"email", max_length=1024, unique=True)
    name = models.CharField(max_length=1024)
    is_active = models.BooleanField(u"can log in", default=True)
    is_admin = models.BooleanField(u"is an administrator", default=False)
    is_deleted = models.BooleanField(u"is deleted", default=False)

    created_date = models.DateTimeField(auto_now_add=True)

    facebook_user = models.OneToOneField(FacebookUser, null=True, related_name="django_user")

    total_cash = models.FloatField(u"ilość gotówki", default=0.)
    total_given_cash = models.FloatField(u"ilość przyznanej gotówki w historii", default=0.)

    USERNAME_FIELD = 'username'

    def get_full_name(self):
        return "%s (%s)" % (self.name, self.username)

    def get_short_name(self):
        return self.name

    def has_perm(self, perm, obj=None):
            return True

    def has_module_perms(self, app_label):
        return True

    def topup_cash(self, amount):
        self.total_cash = F('total_cash') + amount
        self.total_given_cash = F('total_given_cash') + amount

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin