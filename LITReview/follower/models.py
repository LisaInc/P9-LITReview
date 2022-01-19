from django.db import models

from authentication.models import User


class UserFollows(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    followed_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_followed"
    )

    class Meta:
        unique_together = (
            "user",
            "followed_user",
        )
