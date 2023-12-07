import json

from django.core.exceptions import ValidationError
from rest_framework import status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from appointment.models import Appointment
from appointment.serializers import AppointmentSerializer


class AppointmentViewSet(viewsets.GenericViewSet):
    pagination_class = PageNumberPagination

    def list(self, request):
        queryset = Appointment.objects.all()
        professional_id = request.query_params.get('professional_id')

        if professional_id is not None:
            queryset = queryset.filter(professional__id=professional_id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = AppointmentSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AppointmentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        serializer = AppointmentSerializer(data=body)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Appointment.objects.all()
        try:
            appointment = queryset.get(pk=pk)
        except ValidationError as exc:
            raise NotFound("Invalid Id") from exc
        except Appointment.DoesNotExist as exc:
            raise NotFound("Appointment not found") from exc
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Appointment.objects.all()
        try:
            appointment = queryset.get(pk=pk)
        except ValidationError as exc:
            raise NotFound("Invalid Id") from exc
        except Appointment.DoesNotExist as exc:
            raise NotFound("Appointment not found") from exc
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        serializer = AppointmentSerializer(appointment, data=body, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Appointment.objects.all()
        try:
            appointment = queryset.get(pk=pk)
        except ValidationError as exc:
            raise NotFound("Invalid Id") from exc
        except Appointment.DoesNotExist as exc:
            raise NotFound("Appointment not found") from exc
        if appointment:
            appointment.delete()
            return Response(status=204)
        return Response(status=404)

