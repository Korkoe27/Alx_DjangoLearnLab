from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

# ---------------------------
# Library App Models
# ---------------------------
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # Custom permissions
    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='books')

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class CustomUserManager(BaseUserManager):
    """
    Custom user manager for handling user creation with additional fields
    """
    def create_user(self, username, email, password=None, date_of_birth=None, **extra_fields):
        """
        Create and save a regular user with the given username, email, and password
        """
        if not email:
            raise ValueError(('The Email field must be set'))
        if not username:
            raise ValueError(('The Username field must be set'))
        
        email = self.normalize_email(email)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        
        user = self.model(
            username=username,
            email=email,
            date_of_birth=date_of_birth,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, date_of_birth=None, **extra_fields):
        """
        Create and save a superuser with the given username, email, and password
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        
        return self.create_user(username, email, password, date_of_birth, **extra_fields)

# ---------------------------
# Custom User Model
# ---------------------------
class CustomUser(AbstractUser):
    """
    Custom user model extending AbstractUser with additional fields
    """
    date_of_birth = models.DateField(
            ('date of birth'),
        null=True,
        blank=True,
        help_text=('User\'s date of birth')
    )
    profile_photo = models.ImageField(
            ('profile photo'),
        upload_to='profile_photos/',
        null=True,
        blank=True,
        help_text=('User\'s profile photo')
    )
    
    # Use the custom manager
    objects = CustomUserManager()
    
    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')
        ordering = ['-date_joined']
    
    def __str__(self):
        return self.username
    
    def get_age(self):
        """
        Calculate user's age based on date of birth
        """
        if self.date_of_birth:
            from datetime import date
            today = date.today()
            return today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
            )
        return None


# ---------------------------
# UserProfile Model for Roles
# ---------------------------
ROLE_CHOICES = [
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

# Automatically create UserProfile when a new user is registered
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, role='Member')
