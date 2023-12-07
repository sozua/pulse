import json

from django.core.exceptions import ValidationError
from rest_framework import status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from professional.models import Professional
from professional.serializers import ProfessionalSerializer


class ProfessionalViewset(viewsets.GenericViewSet):
    pagination_class = PageNumberPagination 

    def list(self, request):
        queryset = Professional.objects.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ProfessionalSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ProfessionalSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        serializer = ProfessionalSerializer(data=body)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Professional.objects.all()
        try:
            professional = queryset.get(pk=pk)
        except ValidationError as exc:
            raise NotFound("Invalid Id") from exc
        except Professional.DoesNotExist as exc:
            raise NotFound("Professional not found") from exc
        serializer = ProfessionalSerializer(professional)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Professional.objects.all()
        try:
            professional = queryset.get(pk=pk)
        except ValidationError as exc:
            raise NotFound("Invalid Id") from exc
        except Professional.DoesNotExist as exc:
            raise NotFound("Professional not found") from exc
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        serializer = ProfessionalSerializer(professional, data=body, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Professional.objects.all()
        try:
            professional = queryset.get(pk=pk)
        except ValidationError as exc:
            raise NotFound("Invalid Id") from exc
        except Professional.DoesNotExist as exc:
            raise NotFound("Professional not found") from exc
        if professional:
            professional.delete()
            return Response(status=204)
        return Response(status=404)
