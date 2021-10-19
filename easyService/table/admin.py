from django.contrib import admin

from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin
class MyAdminSite(AdminSite):

    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        app_dict = self._build_app_dict(request)

        # Sort the apps alphabetically.
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        # Sort the models alphabetically within each app.
        #for app in app_list:
        #    app['models'].sort(key=lambda x: x['name'])

        return app_list
admin.site = MyAdminSite()


admin.site.register(Group, GroupAdmin)
admin.site.register(User, UserAdmin)
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




from table.models import Type

class TypeAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке
    #list_display = ("name")
    # добавляем интерфейс для поиска по тексту постов
    search_fields = ("name",)
    # добавляем возможность фильтрации по дате
    list_filter = ("name",)


admin.site.register(Type, TypeAdmin)

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


