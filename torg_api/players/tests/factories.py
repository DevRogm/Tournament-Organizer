from players.models import Player
from tournaments.tests.factories import TournamentFactory
import factory


class PlayerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Player
        skip_postgeneration_save = True

    name = factory.Sequence(lambda n: f"Test_player_name_{n}")

    @factory.post_generation
    def tournament(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.tournament.add(*extracted)
