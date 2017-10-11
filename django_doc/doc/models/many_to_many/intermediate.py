from django.db import models

__all__ = (
    'Idol',
    'Group',
    'Membership',
)


class Idol(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)
    debut_date = models.DateField()
    members = models.ManyToManyField(
        Idol,
        through='Membership',
        through_fields=('group', 'idol'),
    )
    # Membership 에 있는 group
    # through, through_fields = Many to Many 두 필드에 선언 ,
    # 이 곳이 소스 필드 타겟은 'Membershipd class의 group, idol

    def __str__(self):
        return self.name

class Membership(models.Model):
    idol = models.ForeignKey(
        Idol,
        on_delete=models.CASCADE,
        related_name='membership_set'
    )
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    recommenders = models.ManyToManyField(
        Idol,
        blank=True,
        related_name='recommend_membership_set',
    )
    joined_date = models.DateField()
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.group.name} ' \
               f'{self.idol.name} ' \
               f'({self.is_active})'