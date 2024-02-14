from ..models import Cheese
import pytest

# Connects our tests with our database
pytestmark = pytest.mark.django_db

def __str__():
    cheese = Cheese.objects.create(
        name="Stracchino", 
        description="Semi-sweet cheese eaten with starches.", 
        firmness=Cheese.Firmness.SOFT,
    )
    assert cheese.__str__() == "Stracchino"
    assert str(cheese) == "Stracchino"
