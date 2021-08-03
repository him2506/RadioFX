from django.shortcuts import render
from .models import Station
# Create your views here.
def station(request):
    hindiStations = Station.objects.filter(Language='Hindi')
    engStations = Station.objects.filter(Language='English')
    print(hindiStations)
    print(engStations)
    params = {'hindiStations': hindiStations, 'engStations': engStations}
    # this is a dictionary. we always send dictionary in render.
    return render(request, 'stations.html', params)

    # topSta = Station.objects.filter(top=True)
    # param ={'topSta':topSta}
    # return render(request,'index.html',param)

    # topSta = Station.objects.filter(top=True)
    # langStats = []

    # hindiStations=[]
    # engStations=[]

    # langSta = Station.objects.values('Language','station_id')
    # .values return Querryset of dictionaries in which key value pair m station aur language corrsponding honge

    # langs = {item['Language'] for item in langSta}
    # yhan set banaya gya taki koi element repeat na ho.

    # for lang in langs:
    #     if lang == 'Hindi':
    # hindiStations = Station.objects.filter(Language = 'Hindi')
            # hindiStations.append(hindiSta)

        # if lang == 'English':
    # engStations = Station.objects.filter(Language = 'English')
            # engStations.append(engSta)

    # print(hindiStations)
    # print(engStations)
    # params = {'hindiStations':hindiStations,'engStations':engStations}
    # return render(request, 'stations.html', params)

    # for lang in langs:
    #     stat = Station.objects.filter(Language = lang)
    #     langStats.append(stat)
    # print(topSta)
    # print(langStats)
    # params ={'langStats':langStats,"topSta":topSta}
    # return render(request,'stations.html',params)


def station_det(request,my_id):
    station = Station.objects.filter(station_id=my_id)
    sta_lang = station[0].Language
    similar_sta = Station.objects.filter(Language = sta_lang)
    st = []
    for item in similar_sta:
        x = item.station_id
        if x != my_id:
            st.append(item)

    return render(request,'station.html',{'station':station[0],'st':st})
