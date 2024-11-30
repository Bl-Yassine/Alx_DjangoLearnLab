from django.db import models
from django.utils.timezone import now
# Create your models here.

# Author model
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
from django.core.exceptions import ValidationError    
def validate_year_not_in_future(value):
    current_year = now().year
    if value > current_year:
        raise ValidationError(f"{value} is in the future. Year must not exceed {current_year}.")

# Book model
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.PositiveIntegerField(validators=[validate_year_not_in_future])
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title




