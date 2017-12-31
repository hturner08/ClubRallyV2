from __future__ import unicode_literals
from itertools import chain
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import datetime
# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)

class Club(models.Model):
    name = models.CharField(max_length=30)
    # id = models.IntegerField(default=Club.objects.all()|length,primary_key=True)
    creator = models.ForeignKey('clubs.User', on_delete=models.CASCADE,blank=True,null=True)
    presidents = models.ManyToManyField('clubs.User',related_name='Co-Presidents+')
    board = models.ManyToManyField('clubs.User', related_name='board members+', blank = True)
    memberList = models.ManyToManyField('clubs.User',related_name='members+', blank = True)
    description = models.CharField(max_length=10000,blank = True)
    creationDate = models.DateField('date created', default = datetime.now)
    weeklyMeetingTime = models.TimeField('Weekly Meeting Time',  default=datetime.now, blank =True)
    Day_Choices = (
    ('M','Monday'),
    ('Tu','Tuesday'),
    ('W','Wednesday'),
    ('Th','Thursday'),
    ('F','Friday'),
    ('Sa','Saturday'),
    ('Su','Sunday'),
    )
    weeklyMeetingDay = models.CharField(max_length=2,choices=Day_Choices,blank=True)
    icon = models.ImageField(upload_to='icons/', default="{%static 'clubs/clubdefault.png'%}", blank=True)
    def count(self):
        return presidents.size + board.size + memberList.size
    def boardPromote(self, member):
        return member;
    def delete(self):
        self.delete()
    def __str__(self):
        return self.name

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff=True
    #Restricted to 12. Don't look at me like that, you know you couldn't be involved in more!
    current_clubs = models.ManyToManyField('clubs.Club', related_name='Clubs+',blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
    def add_club(self,club_id):
        addclub = Club.objects.filter(pk=club_id)
        self.current_clubs.add(club_id)
