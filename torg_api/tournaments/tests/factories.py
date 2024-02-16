
from tournaments.models import Tournament
from django.contrib.auth.models import User
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"Test_username_name_{n}")
    email = "test@user.pl"
    password = "test_password_!!##"



class TournamentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tournament

    name = factory.Sequence(lambda n: f"Test_tournament_name_{n}")
    organizer = factory.SubFactory(UserFactory)
    num_of_players = 4
    description = "Test tournament description"



