from rest_framework import viewsets, mixins
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, FileResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from zipfile import ZipFile
import requests
import pika
import math
import time
import uuid
import threading

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

        url = 'http://localhost:8001/file/zip/'
        key = str(uuid.uuid4())
        header = {
            'X-ROUTING-KEY': key
        }
        files = {'upload_file': uploaded_file}
        data = {
            'filename': uploaded_file.name,
            'size': uploaded_file.size
        }
        requests.post(url, data=data, files=files, headers=header)

        path = '/file/progress/{}/'.format(key)
        return HttpResponseRedirect(path)
    
    return render(request,'upload_form.html', {})

def progress_view(request, key):
    return render(request, 'progressbar.html', {'key': key})

@csrf_exempt
def zip_worker(request):
    if request.method=="POST":
        uploaded_file = request.FILES['upload_file']
        zip_name = '{}.zip'.format(request.POST['filename'])
        file_size = request.POST['size']
        key = str(request.META.get('X-ROUTING-KEY'))

        zipped = ZipperThread(uploaded_file, zip_name, file_size, key)

        resp = {'message': 'Upload successful!'}
        return JsonResponse(resp)


class ZipperThread(object):
    def __init__(self, file, zipname, filesize, key):
        self.zip = ZipFile(zipname, 'w')
        self.file = file
        self.size = filesize
        self.key = key

        credentials = pika.PlainCredentials('0806444524', '0806444524')
        connection = pika.BlockingConnection(pika.ConnectionParameters(
                                                host='152.118.148.95',
                                                port=5672,
                                                virtual_host='/0806444524',
                                                credentials=credentials))
        self.channel = connection.channel()
        self.channel.exchange_declare(exchange='1606828702', exchange_type='direct')

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        self.zip.write(self.file.temporary_file_path())

        byte_per_second = 58407138
        seconds = float(self.size) / byte_per_second
        seconds_per_ten_percent = math.ceil(seconds / 10)

        percent = 10
        while percent <= 100:
            time.sleep(seconds_per_ten_percent)
            self.channel.basic_publish(
                exchange='1606828702',
                routing_key=self.key,
                body=str(percent))