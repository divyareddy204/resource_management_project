import pytest

@pytest.fixture()
def create_user():
    from resource_management_auth.models import User
    user = User.objects.create(username="divya")
    user.set_password("ibhubs@123")
    user.save()
    return user.id