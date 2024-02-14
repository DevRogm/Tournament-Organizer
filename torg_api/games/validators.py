from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class GameResultApproveValidator:

    def __init__(self, score_1="score_1", score_2="score_2", is_approved="is_approved"):
        self.score_1 = score_1
        self.score_2 = score_2
        self.is_approved = is_approved

    def __call__(self, attrs):
        scores_not_exist = not isinstance(attrs[self.score_1], int) or not isinstance(attrs[self.score_2], int)
        scores_draw = attrs[self.score_1] == attrs[self.score_2]
        if (scores_not_exist or scores_draw) and attrs[self.is_approved]:
            message = f"Cannot approve game result without both scores or with draw"
            raise serializers.ValidationError({'is_approved': _(message)})
