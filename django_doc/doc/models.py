from django.db import models

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


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        primary_key=True
    )

class Manufacturer(models.Model):
    name = models.CharField(max_length=50)  # max_length 지정은 꼭필요하다

    def __str__(self):
        return self.name

class Car(models.Model):
    manufacturer = models.ForeignKey(
        # 데이터 상에는 manufacturer_id
        Manufacturer,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50, blank=True)

    # field에 blank = True가 있으면 양식 유효성 검사에서 빈 값을 입력 할 수 있습니다.

    def __str__(self):
        return f'{self.manufacturer.name} - {self.name}'

# many-to-one relationship

class User(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.ForeignKey(
     # teacher가 한 명이라는 가정, 만약 여러명이면 ManytoMany
        'self',
        on_delete=models.SET_NULL,
        # teacher 가 없어져도 다른 관계는 그대로(선생만 없어졌다)
        # on_delete 연결된 객체가 지워졌을 떄를 말하는 것
        blank=True,
        null=True
        # null 값이 들어가기 위해 null True 옵션
    )

    def __str__(self):
        return self.name