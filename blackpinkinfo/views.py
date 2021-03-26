from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BlackpinkSerializers
from .models import Member


@api_view(['GET'])
def get_blackpinkinfo(request):
    if request.method == "GET":
        members = Member.objects.all()
        members_serializers = BlackpinkSerializers(members, many=True)
        return Response(members_serializers.data)
