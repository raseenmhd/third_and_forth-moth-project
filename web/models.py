from django.db import models
from django.core.validators import MinLengthValidator

class user(models.Model):
    name = models.CharField(max_length=50)
    phone = models.PositiveIntegerField(
        validators=[MinLengthValidator(10)]
    )
    email = models.EmailField()
    is_delete = models.BooleanField(default=False)



