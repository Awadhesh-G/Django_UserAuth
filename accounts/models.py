from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    BUYER = 'buyer'
    SELLER = 'seller'
    USER_TYPES = [
        (BUYER, 'Buyer'),
        (SELLER, 'Seller'),
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPES)

    # Provide custom related_name for groups and user_permissions
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='customuser_set',  # Custom related_name
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='customuser_set',  # Custom related_name
        related_query_name='user',
    )
