from django.contrib import admin

from .models import School, Place, Restaurant, Student, Teacher, Champion

class ChampionAdmin(admin.ModelAdmin):   # admin 커스터마이징
    list_display = ('name', 'champion_type', 'rank',)
    list_editable = ('rank',)
    ordering = ('rank',)

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(School)
admin.site.register(Place)
admin.site.register(Restaurant)

admin.site.register(Champion, ChampionAdmin)