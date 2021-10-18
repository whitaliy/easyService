from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import Object
from .models import Buildings
from .models import Type
from .models import Сabinet
from .models import Dir

def tree(request):
# одна строка вместо тысячи слов на SQL
    latestdir = Dir.objects.all()
    latestbiul = Buildings.objects.all()
    latestType = Type.objects.all()
    latest = Object.objects.all()
    latestcab = Сabinet.objects.all()
    #latest = Object.objects.order_by('cabinet')[:10] #В функции index переменная latest получает выборку записей модели Post из БД. После имени модели и специальной точки входа .objects указаны условия запроса.
    #сортируем записи по свойству pub_date по убыванию, от больших значений к меньшим (об этом говорит знак -), то есть новые записи оказываются вверху выборки
    # собираем тексты постов в один, разделяя новой строкой

    output = []
    for item in latest:
        output.append(item.name)


    outputdir = []
    for item in latestdir:
        output.append(item.name)


    #'\n'.join(output)
    return render (request,"tree.html",{"Objects":latest, "Dirs": latestdir, "Buildings": latestbiul, "Types": latestType, "Сabinets": latestcab})