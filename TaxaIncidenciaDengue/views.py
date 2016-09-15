from django.shortcuts import render

# Create your views here.
from pymongo import MongoClient
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from TaxaIncidenciaDengue.TaxaIncidenciaDengue_Utils import updateDb, connectDb, updateDb_Br
from bson.json_util import dumps
import json

# Create your views here.
@api_view(['GET'])
def getTaxaIncidenciaDengueUF(request):
    client = MongoClient()
    db = client.TaxasIncidenciasDengue
    #updateDB()
    incidencias = db.IncidenciasPorUF
    jsonstr = dumps(incidencias.find())
    jsonstrindent = json.loads(jsonstr)
    return Response(jsonstrindent)

@api_view(['GET'])
def getTaxaIncidenciaDengueBrasil(request):
    db = connectDb()
    # updateDb_Br()
    incidencias = db.IncidenciasBrasil
    jsonstr = dumps(incidencias.find())
    jsonstrindent = json.loads(jsonstr)
    return Response(jsonstrindent)