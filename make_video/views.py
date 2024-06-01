from django.shortcuts import render, redirect
from django.http import FileResponse
import os

from movie import create_video
from .forms import TextInputForm
from .models import UserRequest


def text_input_view(request):
    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            user_text = form.cleaned_data['user_text']

            # Запуск скрипта для создания видео
            video_path = os.path.join('media', 'running_text.mp4')
            create_video(user_text, video_path)

            # Сохранение в базу данных
            user_request = UserRequest(text=user_text)
            user_request.save()

            return redirect('download_video')
    else:
        form = TextInputForm()
    return render(request, 'text_input.html', {'form': form})


def download_video(request):
    video_path = os.path.join('media', 'running_text.mp4')
    response = FileResponse(open(video_path, 'rb'), as_attachment=True, filename='running_text.mp4')
    return response
