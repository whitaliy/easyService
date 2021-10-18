from django.contrib import admin




# Register your models here.
from table.models import Dir

class DirAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке
    #list_display = ("name")
    # добавляем интерфейс для поиска по тексту постов
    search_fields = ("name",)
    # добавляем возможность фильтрации по дате
    list_filter = ("name",)


admin.site.register(Dir, DirAdmin)


from table.models import Buildings


class BuildingsAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке
    list_display = ("name", "dir")
    # добавляем интерфейс для поиска по тексту постов
    search_fields = ("name",)
    # добавляем возможность фильтрации по дате
    list_filter = ("name", "dir",)

admin.site.register(Buildings, BuildingsAdmin)


from table.models import Сabinet

class СabinetAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке
    list_display = ("name", "buildings")
    # добавляем интерфейс для поиска по тексту постов
    search_fields = ("name",)
    # добавляем возможность фильтрации по дате
    list_filter = ("name", "buildings",)


admin.site.register(Сabinet, СabinetAdmin)


from table.models import Object




class ObjectAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке
    list_display = ("name", "serial", "type", "cabinet")

    # добавляем интерфейс для поиска по тексту постов
    search_fields = ("name","type__name", "cabinet__name", "cabinet__buildings__dir__name", "cabinet__buildings__name")
    # добавляем возможность фильтрации по дате
    list_filter = ("dir", "buildings", "cabinet", "type", )
    empty_value_display = "-пусто-" # это свойство сработает для всех колонок: где пусто - там будет эта строка


admin.site.register(Object, ObjectAdmin)

from table.models import Type

class TypeAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке
    #list_display = ("name")
    # добавляем интерфейс для поиска по тексту постов
    search_fields = ("name",)
    # добавляем возможность фильтрации по дате
    list_filter = ("name",)


admin.site.register(Type, TypeAdmin)