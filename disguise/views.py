from rest_framework import viewsets, mixins
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, FileResponse, HttpResponseRedirect
from django.urls import reverse
import zipfile
import requests

from .models import Disguise, Document
from .serializers import DisguiseSerializer, DocumentSerializer
from .forms import DisguiseForm, DocumentForm


class DisguiseViewSet(viewsets.ModelViewSet):

    queryset = Disguise.objects.all()
    serializer_class = DisguiseSerializer

class DocumentViewSet(viewsets.ModelViewSet):

    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


def upload_form_view(request):
    if request.method=="POST":
        uploaded_file = request.FILES['myfile']
        return render(request, 'progressbar.html', {})
    
    return render(request,'upload_form.html', {})