from django.db import models

__all__ = (
    'Place',
    'Restaurant',
)


class Place(models.Model):
    name = models.CharField(max_length=50, default='ABC')
    address = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Restaurant(Place): # Place 모델과 join
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} Restaurant'


class Supplier(Place):  # Place에서 상속 받고 있다
    # place_ptr = models.OneToOneField(Place)
    supply_places = models.ManyToManyField(
        Place,
        related_name='supply_place_set',  # query name이 related name으로 대체 된되ㅏ
        related_query_name='supply_place',  # supply_place
    )

    # 데이터를 1번 가져올떄 2개의 테이블을 거쳐야 한다. 성능이 좋지 않다.
    # Place에 연결되어 있는 Restaurant에 접근해 객체를 불러 온다





# In [1]: from inheritance.models.multi_table import *

# In [2]: Place.objects.filter(adc='abd')

# FieldError: Cannot resolve keyword 'adc' into field. Choices are: address, id, name, restaurant, supplier, supply_place


