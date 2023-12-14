from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, User

class Customer(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12)
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        verbose_name='user permissions',
        blank=True,
    )

    def __str__(self):
        return self.username


class Organisation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=512)
    tables = models.PositiveIntegerField(default=0)
    working_hours = models.CharField(max_length=255)
    cuisine = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='organisations_owned')

    def save(self, *args, **kwargs):
        if not self.pk and not self.owner:
            default_user, created = User.objects.get_or_create(username='здесь_ваше_имя_пользователя')
            self.owner = default_user
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(Customer, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'