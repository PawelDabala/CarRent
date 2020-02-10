from django.db import models

# Create your models here.


class User(models.Model):
    """Model definition for User."""

    # TODO: Define fields here
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Address(models.Model):
    """Model definition for Address."""

    # TODO: Define fields here
    street = models.CharField(max_length=50)
    bulding = models.CharField(max_length=50)
    flat = models.CharField(max_length=50)
    post_code = models.DecimalField(max_digits=5, decimal_places=0)
    city = models.CharField(max_length=50)
    users = models.ManyToManyField(User)

    def __str__(self):
        """Unicode representation of Address."""
        return self.street

    
