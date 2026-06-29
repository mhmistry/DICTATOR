from django.db import models
import re  # For character checks

class Password(models.Model):
    word = models.TextField(db_index=True)  # The password string
    length = models.IntegerField(db_index=True)  # Length for quick filtering
    has_upper = models.BooleanField(default=False, db_index=True)
    has_lower = models.BooleanField(default=False, db_index=True)
    has_digit = models.BooleanField(default=False, db_index=True)
    has_symbol = models.BooleanField(default=False, db_index=True)