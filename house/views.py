from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.conf import settings
from django.db.models import Count, Max, Min
from house.models import *


def index_page(request):
    s_list = Street.objects.order_by('name').annotate(house_count=Count('house'))
    h_list = House.objects.all()
    p_list = HousePhoto.objects.all()[:30]
    map_border = h_list.aggregate(Max('coord_lon'), Min('coord_lon'), Max('coord_lat'), Min('coord_lat'))
    if map_border['coord_lat__max'] != None:
        map_center = {
            'lat': (map_border['coord_lat__max'] + map_border['coord_lat__min']) / 2,
            'lon': (map_border['coord_lon__max'] + map_border['coord_lon__min']) / 2,
        }
    else:
        map_center = False

    return render_to_response('house/index.html', {
        'street_list': s_list,
        'house_list': h_list,
        'photo_list': p_list,
        'map_center': map_center,
        'CMADE_KEY': settings.CMADE_KEY,
        }, context_instance=RequestContext(request))


def upload(request):
    s_list = Street.objects.order_by('name').annotate(house_count=Count('house'))
    h_list = House.objects.all()
    map_border = h_list.aggregate(Max('coord_lon'), Min('coord_lon'), Max('coord_lat'), Min('coord_lat'))
    if map_border['coord_lat__max'] != None:
        map_center = {
            'lat': (map_border['coord_lat__max'] + map_border['coord_lat__min']) / 2,
            'lon': (map_border['coord_lon__max'] + map_border['coord_lon__min']) / 2,
        }
    else:
        map_center = False

    return render_to_response('house/upload.html', {
        'street_list': s_list,
        'house_list': h_list,
        'map_center': map_center,
        'CMADE_KEY': settings.CMADE_KEY,
        }, context_instance=RequestContext(request))


def add(request):
    s_list = Street.objects.order_by('name').annotate(house_count=Count('house'))
    h_list = House.objects.all()
    p_list = HousePhoto.objects.all()[:30]
    map_border = h_list.aggregate(Max('coord_lon'), Min('coord_lon'), Max('coord_lat'), Min('coord_lat'))
    if map_border['coord_lat__max'] != None:
        map_center = {
            'lat': (map_border['coord_lat__max'] + map_border['coord_lat__min']) / 2,
            'lon': (map_border['coord_lon__max'] + map_border['coord_lon__min']) / 2,
        }
    else:
        map_center = False

    return render_to_response('house/add.html', {
        'street_list': s_list,
        'house_list': h_list,
        'photo_list': p_list,
        'map_center': map_center,
        'CMADE_KEY': settings.CMADE_KEY,
        }, context_instance=RequestContext(request))


def street(request, id):
    s = Street.objects.get(pk=id)
    s_list = Street.objects.order_by('name').annotate(house_count=Count('house'))
    h_list = House.objects.filter(street=id).order_by('number')
    map_border = h_list.aggregate(Max('coord_lon'), Min('coord_lon'), Max('coord_lat'), Min('coord_lat'))
    if map_border['coord_lat__max'] != None:
        map_center = {
            'lat': (map_border['coord_lat__max'] + map_border['coord_lat__min']) / 2,
            'lon': (map_border['coord_lon__max'] + map_border['coord_lon__min']) / 2,
        }
    else:
        map_center = False

    return render_to_response('house/street.html', {
        'street': s,
        'street_list': s_list,
        'house_list': h_list,
        'map_center': map_center,
        'CMADE_KEY': settings.CMADE_KEY,
        }, context_instance=RequestContext(request))


def house(request, id):
    h = House.objects.get(pk=id)
    s_list = Street.objects.order_by('name').annotate(house_count=Count('house'))
    photo = HousePhoto.objects.filter(house=h)

    return render_to_response('house/house.html', {
        'house': h,
        'street_list': s_list,
        'photo': photo,
        'is_admin': True,
        'CMADE_KEY': settings.CMADE_KEY,
        }, context_instance=RequestContext(request))

