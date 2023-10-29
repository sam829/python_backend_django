from django.shortcuts import render
from rest_framework import viewsets
from .models import Notes, Customer
from .serializers import NotesSerializer, CustomerSerializer


# Create your views here.
class NotesViewSet(viewsets.ModelViewSet):
    serializer_class = NotesSerializer
    queryset = Notes.objects.all()


class CustomerCreate(viewsets.generics.CreateAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class CustomerList(viewsets.generics.ListAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class CustomerDetail(viewsets.generics.RetrieveAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class CustomerUpdate(viewsets.generics.RetrieveUpdateAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class CustomerDelete(viewsets.generics.RetrieveDestroyAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
