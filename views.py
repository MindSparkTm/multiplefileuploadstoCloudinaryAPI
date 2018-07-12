from django import forms
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from django.shortcuts import render, redirect, reverse

from cloudinary.forms import cl_init_js_callbacks
from .models import Photo
from .forms import PhotoForm
from django.views.generic import DetailView, ListView, UpdateView, CreateView, View
import cloudinary
import cloudinary.uploader
import cloudinary.api

class upload(CreateView):

  model = Photo

  def get(self,request):

    return render (request,'kmd/upload.html')

  def post(self, request):
        title = request.POST['title']
        description = request.POST['description']






        if len(request.FILES['uploadedfile']) != 0:
          cloudinary.config(
            cloud_name="mobiotrics",
            api_key="841164352818738",
            api_secret="tlEgZOo2TiK34J-kQ9BBqwUM4mg"
          )

          for file in request.FILES.getlist('uploadedfile'):
              fs = FileSystemStorage()

              res = cloudinary.uploader.upload(file)
              publicid= res['public_id']
              url = res['url']
              print('response',res['public_id'])
              filename = fs.save(file.name, file)
              photo = Photo(title=title, description=description, publicid=publicid, url=url,
                       )
              photo.save()

        return render(request, 'kmd/upload.html')

class videoupload(CreateView):

      model = Photo

      def get(self, request):

          return render(request, 'kmd/videoupload.html')

      def post(self, request):
          print('Videokksks')
          title = request.POST['title']
          description = request.POST['description']

          if len(request.FILES['uploadedfile']) != 0:
              cloudinary.config(
                  cloud_name="mobiotrics",
                  api_key="841164352818738",
                  api_secret="tlEgZOo2TiK34J-kQ9BBqwUM4mg"
              )

              for file in request.FILES.getlist('uploadedfile'):
                  fs = FileSystemStorage()

                  res = cloudinary.uploader.upload(file,resource_type = "video", chunk_size = 1000000)
                  publicid = res['public_id']
                  url = res['url']
                  print('response', res['public_id'])
                  filename = fs.save(file.name, file)
                  photo = Photo(title=title, description=description, publicid=publicid, url=url,
                                )
                  photo.save()

          return render(request, 'kmd/videoupload.html')
