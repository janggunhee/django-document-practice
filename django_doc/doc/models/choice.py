from django.db import models

__all__ = (
    'Person',
)
# person만 import 하겠다

class Person(models.Model):   # person은 실제 database의 table이 된다

    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    # 클래스 이름 속성으로 지정 각 속성은 데이터 베이스  column에 맵핑
