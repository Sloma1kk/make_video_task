from moviepy.editor import TextClip, CompositeVideoClip, ColorClip


def create_video(user_text, video_path):
    # Параметры видео
    video_width = 100
    video_height = 100
    duration = 3  # продолжительность видео в секундах

    # Создание фона
    background_clip = ColorClip(size=(video_width, video_height), color=(255, 255, 255), duration=duration)

    # Параметры текста
    text = user_text
    fontsize = 50
    color = 'black'

    # Создание текстового клипа
    text_clip = TextClip(text, fontsize=fontsize, color=color, font="Arial")

    # Определение начальной и конечной позиций текста
    text_width, text_height = text_clip.size
    start_position = (video_width, (video_height - text_height) // 2)

    # Анимация текста с помощью set_position
    text_clip = text_clip.set_position(
        lambda t: (
            start_position[0] - t * (video_width + text_width) / duration, start_position[1])).set_duration(duration)

    # Создание финального клипа
    final_clip = CompositeVideoClip([background_clip, text_clip])

    # Сохранение видео в файл
    final_clip.write_videofile(video_path, fps=60)


if __name__ == '__main__':
    create_video('Бегущая строка', '/media/running_text.mp4')
