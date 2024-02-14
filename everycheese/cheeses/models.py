from django.db import models
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel

class Cheese(TimeStampedModel):
    name = models.CharField("Name of Cheese", max_length=255)
    slug = AutoSlugField("Cheese Address", unique=True, always_update=False, populate_from="name")
    description = models.TextField("Description", blank=True)

    class Firmness(models.TextChoices):
        UNSPECIFIED = "unspecified", "Unspecified"
        SOFT = "soft", "Soft"
        SEMI_SOFT = "semi-soft", "Semi-Soft"
        SEMI_HARD = "semi-hard", "Semi-Hard"
        HARD = "hard", "Hard"
    
    firmness = models.CharField("Firmness", max_length=20, choices=Firmness.choices, default=Firmness.UNSPECIFIED)

# Create an instance of Cheese
cheese = Cheese(name="Cheddar", firmness=Cheese.Firmness.SOFT)

# Now you can check the firmness
if cheese.firmness == Cheese.Firmness.SOFT:
    print("This cheese is soft!")

def __str__(self):
    return self.name
