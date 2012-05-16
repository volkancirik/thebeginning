# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def render_response(req, *args, **kwargs):
    kwargs['context_instance'] = RequestContext(req)
    return render_to_response(*args, **kwargs)

def background(request):
    return render_response(request, 'background.html', {  })

def video(request):
   return render_response(request, 'video.html', {  })

def gallery(request):
    image_index = [ 1,2,3,4,5,6,7,8,9,10,11,12,13]
    return render_response(request, 'gallery.html', { 'image_index' : image_index })

class cast:
    def __init__(self, baslik, kisi):
        self.baslik = baslik
        self.kisi = kisi


def castandcrew(request):

#    item =  cast('basliktext','kisitext')

    itemlist = []
    crewlist = []

    item = cast('','')
    itemlist.append(item)

    item = cast('Storied and Directed by ','Yigit Evgar')
    itemlist.append(item)

    item = cast('Written by ','Eset Akcilad')
    itemlist.append(item)


    item = cast('Produced by','Multi Arts Production')
    itemlist.append(item)

#Duygu     Demet Evgar
#Yuksel    Oner Erkan
#Elif         Ece cesmioglu
#Mother    Bingul Evgar
#Efe         Efe Sakiz
#Collection Agent      Levent Evgar
#Hospital Lawyer       Can Yilmaz
#Child Duygu        Aslihan Gencay
#Child Efe           Alper Patan
#Mover 1          Selahattin Korkmaz
#Mover 2          Sadik Sav


    item = cast('Director of Photography','Cengizhan Cebeci')
    crewlist.append(item)

    item = cast('Editor','Burcak Yurdakul-Yigit Evgar')
    crewlist.append(item)

    item = cast('Music','Selim Siyami Sumer')
    crewlist.append(item)


    item = cast('Lighting','Turgut Kucuk')
    crewlist.append(item)


    item = cast('Location Sound','Onur Yavuz')
    crewlist.append(item)

    item = cast('Art Director','Melis Binay')
    crewlist.append(item)

    item = cast('Hair','Ibrahim Zengin')
    crewlist.append(item)


    item = cast('Make-up','Fatka Kardes-Cigdem Uzundag')
    crewlist.append(item)

    item = cast('Dolly','Mehmet Ali Mendi')
    crewlist.append(item)

    item = cast('Dolly assistant','Murat Koc')
    crewlist.append(item)

    item = cast('Camera Assistant1','Enver Serihat')
    crewlist.append(item)

    item = cast('Camera Assistant 2','Erdal Yilmaz')
    crewlist.append(item)

    item = cast('Boom Operator','Goktay Bektas')
    crewlist.append(item)

    item = cast('Ligting Gapper','Hakan Dokurlar')
    crewlist.append(item)

    item = cast('Line producer','Murat Akbel')
    crewlist.append(item)

    item = cast('Set Photographer','Deniz Unlusu - Selin Demircioglu')
    crewlist.append(item)



    item = cast('Nitris Color','Mustafa Tasitman')
    crewlist.append(item)


    item = cast('Visual Effects','Mustafa Tasitman - Erkan Cerit')
    crewlist.append(item)

    item = cast('Ses mix','Gokhan Pinar')
    crewlist.append(item)


    item = cast('Poster Design','Hatice Pamuk')
    crewlist.append(item)

    item = cast('Website','Volkan Cirik')
    crewlist.append(item)



    item = cast('Subtitle Translator','Esra Ozturk')
    crewlist.append(item)

#
#    itemlist.append(item)
    
    return render_response(request, 'castandcrew.html', { 'production' : itemlist ,'crew' : crewlist})
def director(request):
    return render_response(request, 'director.html', {  })

def contact(request):
    return render_response(request, 'contact.html', {  })
