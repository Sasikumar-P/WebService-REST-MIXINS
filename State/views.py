# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Country
from serializers import CountrySerializer 
from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics

class CountryList(mixins.RetrieveModelMixin,mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView, mixins.CreateModelMixin):

	queryset = Country.objects.all()
	serializer_class = CountrySerializer

        def get(self, request, *args, **kwargs):
        	return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
        	return self.create(request, *args, **kwargs)

class CountryDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
	queryset = Country.objects.all()
        serializer_class = CountrySerializer

        def get(self, request, *args, **kwargs):
		 return self.retrieve(request, *args, **kwargs)

        def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

        def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)


# Create your views here.
