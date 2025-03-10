from django.db import models


from django.contrib.auth.models import AbstractUser ,BaseUserManager ,User

class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    
    # date_of_birth: A date field.
    # profile_photo: An image field.


class CustomUserManager(BaseUserManager):
    
    # create_user: Ensure it handles the new fields correctly.
    # create_superuser: Ensure administrative users can still be created with the required fields.
    def create_user(self , date_of_birth , profile_photo):
        
        user = self.model(date_of_birth = date_of_birth,profile_photo = profile_photo)
        return user

        
    def create_super_user():
        pass


class Book(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("can_view", "Can view article"),
            ("can_create", "Can create article"),
            ("can_edit", "Can edit article"),
            ("can_delete", "Can delete article"),
        ]

    def __str__(self):
        return self.title
