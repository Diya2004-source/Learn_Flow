from django.db import models

class User(models.Model):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("student", "Student"),
        ("instructor", "Instructor"),
    )

    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)  # unique for login
    password = models.CharField(max_length=200)  # hashed password
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="student")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
