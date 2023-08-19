from django.shortcuts import render, redirect
from .forms import VideoForm
from .models import Video
from django.shortcuts import get_object_or_404, redirect
import os
from django.conf import settings
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from moviepy.editor import *


# ... (otras importaciones y código) ...





def inicio(request):
    return render(request, 'inicio.html')

def personajes(request):
    return render(request, 'personajes.html')


def generate_thumbnail(video_file):
    video = VideoFileClip(video_file.path)
    thumbnail = video.get_frame(8)  # Captura un cuadro en el quinto segundo del video
    thumbnail_image = Image.fromarray(thumbnail)
    
    # Aumenta el tamaño y ajusta la calidad de la miniatura
    thumbnail_image.thumbnail((200, 200))
    
    thumbnail_buffer = BytesIO()
    thumbnail_image.save(thumbnail_buffer, format='JPEG', quality=90)
    thumbnail_file = InMemoryUploadedFile(
        thumbnail_buffer, None, 'temp.jpg', 'image/jpeg', thumbnail_buffer.tell(), None
    )
    
    return thumbnail_file


# ...




# ...

def subir_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.save()

            # Generar y guardar la miniatura
            video_thumbnail = generate_thumbnail(video.video_file)
            video.thumbnail.save(video.title + '_thumbnail.jpg', video_thumbnail, save=True)  # Asegúrate de que la miniatura se guarda en el modelo Video
            
            return redirect('subirVideo')
    else:
        form = VideoForm()
    return render(request, 'subirVideo.html', {'form': form})


def mostrar_videos(request):
    videos = Video.objects.all()
    return render(request, 'mostrar_videos.html', {'videos': videos})


def video_list(request):
    videos = Video.objects.all()
    context = {'videos': videos}
    return render(request, 'video_list.html', context)

# views.py

# ... (otras importaciones) ...

def delete_video(request, video_id):
    try:
        video = Video.objects.get(id=video_id)
        archivo = video.video_file.path
        video.delete()
        
        # Eliminar el archivo físico
        if os.path.exists(archivo):
            os.remove(archivo)
            
            # También puedes eliminar el directorio vacío si lo deseas
            # os.path.dirname(archivo) obtiene la carpeta del archivo
            # os.rmdir(os.path.dirname(archivo))
            
            mensaje = "Video eliminado correctamente"
            estado = True
        else:
            mensaje = "El archivo no existe"
            estado = False
    except Video.DoesNotExist:
        mensaje = "El video no existe"
        estado = False
    except Exception as error:
        mensaje = str(error)
        estado = False
    
    retorno = {
        "mensaje": mensaje,
        "estado": estado
    }
    
    videos = Video.objects.all()
    retorno['videos'] = videos  # Agrega la lista de videos al contexto
    return render(request, "video_list.html", retorno)  # Renderiza la misma página
