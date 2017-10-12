from django.db import models

__all__ = (
    'Champion',
    'Supporter',
)

# custom manager를 만들고 이 custom manager 를
# proxy 모델에 붙이면 실제 테이블은 1개 이지만 마치 데이터 테이블이
# 따로 있는 것 처럼 쓸 수 있다
# Champion 전체에 대해서 query를 날릴때에도 각각에 대해서 날릴때 에도
# 효율적으로 사용할 수 있다


# class ChampionInfo(models.Model):
#     nickname = models.CharField(max_length=30)
#
#     class Meta:
#         abstract = True


class Champion(models.Model):
    CHOICES_TYPE = (
        ('magician', '마법사'),
        ('supporter', '서포터'),
        ('ad', '원거리 딜러'),
    )
    champion_type = models.CharField(max_length=20, choices=CHOICES_TYPE)
    rank = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name} ({self.get_champion_type_display()})'



class SupporterManager(models.Manager):
    def get_queryset(self):
        return  super().get_queryset().filter(champion_type='supporter')

class Supporter(Champion):
    objects = SupporterManager()

    class Meta:
        proxy = True

    def buy_supporter_item(self):
        print(f'{self.name}은 서포터 아이템을 샀다')

class Midliner(Champion):
    class Meta:
        proxy = True

    def go_to_mid(self):
        print(f'{self.name}은 미드에 도착했다')
