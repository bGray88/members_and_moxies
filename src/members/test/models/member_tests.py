import pytest
from members.models import Member

@pytest.mark.django_db
def test_create_member():
  member = Member.objects.create(
      firstname   = "Claire",
      lastname    = "Redfield",
      phone       = "5555225",
      joined_date = "1999-01-01"
    )
  assert member.firstname == "Claire"
