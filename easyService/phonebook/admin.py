from django.contrib import admin

from .models import Department


class DepartmentAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке
    list_display = ("name",)
    # добавляем интерфейс для поиска по тексту постов
    search_fields = ("name",)
    # добавляем возможность фильтрации по дате
    list_filter = ("name",)

admin.site.register(Department, DepartmentAdmin)


from .models import MAN


class MANAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке
    list_display = ("name","position","department","tel","mobtel","cab","email")
    # добавляем интерфейс для поиска по тексту постов
    search_fields = ("name",)
    # добавляем возможность фильтрации по дате
    list_filter = ("name","department",)

admin.site.register(MAN, MANAdmin)