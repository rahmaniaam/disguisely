from rest_framework import viewsets, mixins
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, FileResponse, HttpResponseRedirect
from django.urls import reverse
from zipfile import ZipFile
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

        url = 'https://localhost:8001/file/zip'
        header = {
            'X-ROUTING-KEY': ''
        }
        data = {
            'file': uploaded_file,
            'filename': uploaded_file.name
        }
        requests.post()
        return render(request, 'progressbar.html', {})
    
    return render(request,'upload_form.html', {})

def zip_worker(request):
    if request.method=="POST":
        uploaded_file = request.data.file
        zip_name = '{}.zip'.format(request.data.filename)

        zip_file = ZipFile(zip_name,'w') 
        zip_file.write(uploaded_file)

    #     return render(request, 'progressbar.html', {})
    
    # return render(request,'upload_form.html', {})