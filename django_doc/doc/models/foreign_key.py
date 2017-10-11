from django.db import models

__all__ = (
    'Car',
    'Manufacturer',
    'User',
)

class Car(models.Model):
    manufacturer = models.ForeignKey(
        # 데이터 상에는 manufacturer_id
        'Manufacturer',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50, blank=True)

    # field에 blank = True가 있으면 양식 유효성 검사에서 빈 값을 입력 할 수 있습니다.

    def __str__(self):
        return f'{self.manufacturer.name} - {self.name}'

class Manufacturer(models.Model):
    name = models.CharField(max_length=50)  # max_length 지정은 꼭필요하다

    def __str__(self):
        return self.name

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

    def save(self, *args, **kwargs):
        print('User save')
        if self.teacher and self.teacher.pk == self.pk:
            print('teacher cannot self')
            self.teacher = None
        super().save(*args, **kwargs)