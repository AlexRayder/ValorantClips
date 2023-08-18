from django.shortcuts import render, redirect
from .forms import VideoForm
from .models import Video
from django.shortcuts import get_object_or_404, redirect


def inicio(request):
    return render(request, 'inicio.html')

def personajes(request):
    return render(request, 'personajes.html')


def subir_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mostrar_videos')
    else:
        form = VideoForm()
    return render(request, 'subirVideo.html', {'form': form})


# ... (otras vistas) ...

def mostrar_videos(request):
    videos = Video.objects.all()
    return render(request, 'mostrar_videos.html', {'videos': videos})


def video_list(request):
    videos = Video.objects.all()
    context = {'videos': videos}
    return render(request, 'video_list.html', context)

def delete_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if request.method == 'POST':
        video.delete()
    return redirect('video_list')


