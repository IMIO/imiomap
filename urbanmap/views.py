from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.gis.geos import GEOSGeometry
from django.core.serializers import serialize
from django.db.models import Max
from django.contrib.gis.gdal import CoordTransform, SpatialReference

from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt

import logging

from urbanmap.models import Parcels, Capa

logger = logging.getLogger(__name__)

def index(request):
    return HttpResponse("UrbanMap")

@csrf_exempt
@require_POST
def get_parcels_light_by_geom(request):
      """
        geom : WKT geometry expected
        perform spatial filter to the cadastral spatial parcel table
      """
      # TODO: input check and error handling
      geom_wkt = request.POST.get("geom")
      try:
            input_geometry = GEOSGeometry(geom_wkt, srid=31370)
            capa_qry = Capa.objects.filter(the_geom__intersects=input_geometry)
            #capa_qry = Parcels.objects.filter(capakey__the_geom__intersects=input_geometry).aggregate(Max('datesituation'))
            logger.error(capa_qry)
            response_geojson = serialize('geojson', capa_qry,
                  geometry_field='the_geom',
                  srid=31370,
                  fields=('capakey'))

            return HttpResponse(response_geojson, content_type='application/json')
      except TypeError as e:
            logger.error(str(e))
            return HttpResponse("Error reading the geometry from geom parameter", status=500)

@csrf_exempt
@require_GET
def get_parcels_by_capakey(request, capakeys):

    # TODO: input check and error handling
    capakeys_parsed = capakeys.split(',')

    capa_qry = Capa.objects.filter(capakey__in=capakeys_parsed)
    
    response_geojson = serialize('geojson', capa_qry,
          geometry_field='the_geom',
          srid=31370,
          fields=('capakey'))
    
    return HttpResponse(response_geojson, content_type='application/json')