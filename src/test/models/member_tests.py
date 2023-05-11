import pytest
from members.models import Member
from test.fixtures.member import db_member

@pytest.mark.django_db
def test_create_member(db_member):
  member = db_member
  assert member.firstname   == "Claire"
  assert member.lastname    == "Redfield"
  assert member.phone       == "5555225"
  assert member.joined_date == "1999-01-01"
