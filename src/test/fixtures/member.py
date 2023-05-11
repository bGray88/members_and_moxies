import pytest
from members.models import Member

@pytest.fixture(autouse=True, scope="function")
def db_member():
  member = Member.objects.create(
    firstname   = "Claire",
    lastname    = "Redfield",
    phone       = "5555225",
    joined_date = "1999-01-01"
  )
  return member