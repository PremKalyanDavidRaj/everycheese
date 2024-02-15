from ..models import Cheese
import pytest

# Connects our tests with our database
pytestmark = pytest.mark.django_db

def __str__():
    cheese = CheeseFactory()
    assert cheese.__str__() == cheese.name
    assert str(cheese) == cheese.name
