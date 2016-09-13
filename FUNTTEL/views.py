from django.shortcuts import render

# Create your views here.
from pymongo import MongoClient
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from FUNTTEL.FUNTTEL_Utils import updateDB
from bson.json_util import dumps
import json
from collections import OrderedDict


@api_view(['GET'])
def getTaxaRetorno(request):
    client = MongoClient()
    db = client.FUNTTEL
    retorno = db.ImpactoSócioeconômicoTaxadeRetorno
    jsonstr = dumps(retorno.find())
    jsonstrindent = json.loads(jsonstr)
    #updateDB()
    return Response(jsonstrindent)

@api_view(['GET'])
def getGeracaoEmprego(request):
    client = MongoClient()
    db = client.FUNTTEL
    empregos = db.ImpactoSócioeconômicoGeraçãodeEmpregos
    jsonstr = dumps(empregos.find())
    jsonstrindent = json.loads(jsonstr)
    #updateDB()
    return Response(jsonstrindent)