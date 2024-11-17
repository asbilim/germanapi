from django.db import models
import uuid

class BaseVocabulary(models.Model):
    """
    Abstract base class for vocabulary items
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    german = models.CharField(max_length=100, unique=True)
    english = models.CharField(max_length=100)
    french = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ['german']

class Country(BaseVocabulary):
    """
    Represents a country name in different languages
    """
    article = models.CharField(max_length=3, help_text="German article (der/die/das)")
    capital = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "countries"

    def __str__(self):
        return f"{self.article} {self.german}"

class Profession(BaseVocabulary):
    """
    Represents a profession in different languages
    """
    article = models.CharField(max_length=3, help_text="German article (der/die/das)")
    feminine_form_german = models.CharField(max_length=100, null=True, blank=True)
    feminine_form_french = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.german

class Animal(BaseVocabulary):
    """
    Represents an animal in different languages
    """
    article = models.CharField(max_length=3, help_text="German article (der/die/das)")
    plural_german = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.article} {self.german}"

class Color(BaseVocabulary):
    """
    Represents a color in different languages
    """
    hex_code = models.CharField(max_length=7, null=True, blank=True, help_text="e.g., #FF0000")

    def __str__(self):
        return self.german

class FoodItem(BaseVocabulary):
    """
    Represents a food item in different languages
    """
    article = models.CharField(max_length=3, help_text="German article (der/die/das)")
    category = models.CharField(max_length=50, choices=[
        ('FRUIT', 'Fruit'),
        ('VEGETABLE', 'Vegetable'),
        ('MEAT', 'Meat'),
        ('DAIRY', 'Dairy'),
        ('GRAIN', 'Grain'),
        ('OTHER', 'Other')
    ])

    def __str__(self):
        return f"{self.article} {self.german}"

class BodyPart(BaseVocabulary):
    """
    Represents a body part in different languages
    """
    article = models.CharField(max_length=3, help_text="German article (der/die/das)")
    plural_german = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.article} {self.german}"

class WeatherTerm(BaseVocabulary):
    """
    Represents weather-related terms in different languages
    """
    category = models.CharField(max_length=50, choices=[
        ('CONDITION', 'Weather Condition'),
        ('TEMPERATURE', 'Temperature'),
        ('PRECIPITATION', 'Precipitation'),
        ('WIND', 'Wind'),
        ('OTHER', 'Other')
    ])

    def __str__(self):
        return self.german