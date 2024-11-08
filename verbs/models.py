from django.db import models
import uuid

class VerbCharacteristic(models.Model):
    """
    Represents a characteristic of a German verb (e.g., strong, modal, etc.).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Verb(models.Model):
    """
    Represents a German verb.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    infinitive = models.CharField(max_length=100, unique=True)
    preterit = models.CharField(max_length=100, null=True, blank=True)
    perfect = models.CharField(max_length=100, null=True, blank=True)
    characteristics = models.ManyToManyField(VerbCharacteristic, related_name='verbs')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.infinitive