from django.db import models

__all__ = (
    'FacebookUser',
)


class FacebookUser(models.Model):
    # 자기자신 (TwitterUser ('self'))를 참조해서
    # friends 필더를 MTM으로 정의
    name = models.CharField(max_length=30)
    friends = models.ManyToManyField(
        'self',
        blank=True,
    )

    def __str__(self):
        return self.name
