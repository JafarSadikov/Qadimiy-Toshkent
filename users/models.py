from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


from users.managers import UserManager

class Role(Group):
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Role')
        verbose_name_plural = _('Roles')

class CustomUser(AbstractUser):
    class Gender(models.TextChoices):
        MALE = 'MALE', 'MALE'
        FEMALE = 'FEMALE', 'FEMALE'

    username = models.CharField(_('username'), max_length=150, blank=True, null=True) 
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['username'],  # unikal bo'lishi kerakli maydon nomi
                name='unique_username'  # unikal bo'lishi kerakli nom
            )
        ]
    phone = PhoneNumberField(unique=True, blank=True, null=True)
    first_name = None
    last_name = None
    full_name = models.CharField(_('full name'), max_length=100, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True, null=True, blank=True)
    roles = models.ManyToManyField(
        Role,
        verbose_name=_("role"),
        blank=True,
        help_text=_(
            "The roles this user belongs to. A user will get all permissions "
            "granted to each of their roles."
        ),
        related_name="custom_users",  # Changed related_name to avoid clash
        related_query_name="user_single",
    )
    age = models.PositiveIntegerField(_('age'), blank=True, null=True)
    gender = models.CharField(_('gender'), max_length=10, choices=Gender.choices, blank=True, null=True)
    # weight = models.PositiveIntegerField(_('weight'), blank=True, null=True)
    # height = models.PositiveIntegerField(_('height'), blank=True, null=True)
    # bmi = models.FloatField(_('bmi'), blank=True, null=True)
    image = models.ImageField(upload_to='users/', blank=True, null=True)

    USERNAME_FIELD = 'phone'
    objects = UserManager()

    def __str__(self):
        return f"{self.phone}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['phone'], name='unique_phone')
        ]
    