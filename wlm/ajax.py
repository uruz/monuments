# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from utils.leaflet_transform import Point, Tile

from wlm.models import Monument


def get_tile_markers(request, x_tile, y_tile, zoom, first, last):
    point = Point(int(x_tile), int(y_tile))
    tile = Tile.tileByPoint(point, int(zoom))
    latlng_min, latlng_max = tile.getBounds()
    monuments = Monument.objects.filter(
        coord_lon__gte=latlng_min.lng,\
        coord_lon__lt=latlng_max.lng,\
        coord_lat__gte=latlng_min.lat,\
        coord_lat__lt=latlng_max.lat).values("id", "coord_lon", "coord_lat", "name").order_by('id')[first:last]
    return render_to_response('markers.js', {'monuments':monuments,}, mimetype='application/json')


def get_tile_markers_count(request, x_tile, y_tile, zoom):
    point = Point(int(x_tile), int(y_tile))
    tile = Tile.tileByPoint(point, int(zoom))
    latlng_min, latlng_max = tile.getBounds()
    mon_count = Monument.objects.filter(
        coord_lon__gte=latlng_min.lng,\
        coord_lon__lt=latlng_max.lng,\
        coord_lat__gte=latlng_min.lat,\
        coord_lat__lt=latlng_max.lat).values("id", "coord_lon", "coord_lat", "name").count()
    return render_to_response('markers_count.js', {'count':mon_count, }, mimetype='application/json')

def test_tile_markers(request, x_tile, y_tile, zoom, first, last):
    point = Point(int(x_tile), int(y_tile))
    tile = Tile.tileByPoint(point, int(zoom))
    latlng_min, latlng_max = tile.getBounds()
    monuments = Monument.objects.filter(
        coord_lon__gte=latlng_min.lng,\
        coord_lon__lt=latlng_max.lng,\
        coord_lat__gte=latlng_min.lat,\
        coord_lat__lt=latlng_max.lat).values("id", "coord_lon", "coord_lat", "name").order_by('id')[first:last]
    return render_to_response('markers.html', {'monuments':monuments,})

