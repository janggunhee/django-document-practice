from django.db import models

class Blog(models.Model):
    name = models.CharField(
        max_length=100,
        blank=True
    )
    tagline = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE
    )
    headline = models.CharField(max_length=255)
    body_text = models.TextField(blank=True)
    Pub_date = models.DateField(
        blank=True, null=True
    )
    mod_date = models.DateField(
        blank=True, null=True
    )
    authors = models.ManyToManyField(Author)   # 저자가 여러명 ;
    n_comments = models.IntegerField(default=0)
    n_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.healine





