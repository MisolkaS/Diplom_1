import pytest
from praktikum.database import *

@pytest.fixture
def db():
    database = Database()
    return database
