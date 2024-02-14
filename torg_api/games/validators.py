from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class GameResultApproveValidator:

    def __init__(self, score_1="score_1", score_2="score_2", is_approved="is_approved"):
        self.score_1 = score_1
        self.score_2 = score_2
        self.is_approved = is_approved

    def __call__(self, attrs):
        if not attrs[self.score_1] or not attrs[self.score_2] and attrs[self.is_approved]:
            message = f"Cannot approve game result without both scores"
            raise serializers.ValidationError({'is_approved': _(message)})
