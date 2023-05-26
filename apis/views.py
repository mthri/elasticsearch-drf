from django.db import transaction

from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from elasticsearch_dsl import Q
from rest_framework.pagination import LimitOffsetPagination

from apis.serializers import CarSerializer
from shop.models import Car
from shop.documents import CarDocument
from apis.permissions import CreateCarPermissions, SearchCarPermissions



class CarCreateUpdateView(generics.CreateAPIView, generics.UpdateAPIView):
    allowed_methods = ['POST', 'PUT']
    permission_classes = (CreateCarPermissions, )
    serializer_class = CarSerializer

    @transaction.atomic
    def put(self, request, *args, **kwargs):
        pk = request.data['id']
        
        # lock on the record
        instance = Car.objects.select_for_update().get(pk=pk)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        
        validated_data = serializer.validated_data
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return Response(serializer.data)


class SearchCarView(APIView, LimitOffsetPagination):
    permission_classes = (SearchCarPermissions, )  
    
    def get(self, request):
        _id = request.query_params.get('id')
        name = request.query_params.get('name')
        num_cylinders = request.query_params.get('num_cylinders')
        num_seats = request.query_params.get('num_seats')
        color = request.query_params.get('color')
        engine_capacity = request.query_params.get('engine_capacity')

        search = CarDocument.search()
        filters = []

        # build the filter conditions based on the query parameters
        if _id:
            filters.append(Q('match', id=_id))
        if name:
            filters.append(Q('match', name=name))
        if num_cylinders:
            filters.append(Q('match', num_cylinders=num_cylinders))
        if num_seats:
            filters.append(Q('match', num_seats=num_seats))
        if color:
            filters.append(Q('match', color=color))
        if engine_capacity:
            filters.append(Q('match', engine_capacity=engine_capacity))

        # apply the filter conditions to the search query
        if filters:
            search = search.query('bool', filter=filters)

        response = search.execute()
        results = self.paginate_queryset(response, request, view=self)
        serializer = CarSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)
    
