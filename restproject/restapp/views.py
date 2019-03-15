from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
class SongsList(APIView):
	def get(self,request):
		song1 = Song.objects.all()
		serializer = SongsSerializer(song1, many=True)
		return Response(serializer.data)

	def post():
		pass

