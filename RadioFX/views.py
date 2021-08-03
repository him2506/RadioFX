from django.shortcuts import render
from stations.models import Station
from django.http import HttpResponse

# def index(request):
#     return render(request, 'index.html')

def index(request):
    topSta = Station.objects.filter(top=True)
    param ={'topSta':topSta}
    print(topSta)
    return render(request,'index.html',param)


    # topSta = Station.objects.filter(top=True)
    #
    # langStats = []
    # langSta = Station.objects.values('Language','station_id')
    # langs = {item['Language'] for item in langSta}
    # for lang in langs:
    #     stat = Station.objects.filter(Language = lang)
    #     # n = len(prod)
    #     # nSlides = (n//4)+ ceil((n/4)-(n//4))
    #     langStats.append(stat)
    #
    # params ={'langStats':langStats,"topSta":topSta}
    # return render(request,'index.html',params)
    
def about(request):
    return render(request,'about.html')