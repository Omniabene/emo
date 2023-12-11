from moviepy.editor import VideoFileClip
from TestEmotionDetector import analyze_video_emotions
from golos import analyze_emotion_from_audio
from aiogram.types import Message, VideoNote, Video
from aiogram import Bot

def determine_final_emotion(emoV, emoG):

    voice_emotion = emoG
    video_emotion = emoV


    # Если по голосу первая эмоция "Neutral", отправляем "Neutral"
    if voice_emotion == "neutral":
        return "Neutral"

    # Если по голосу первая эмоция "Sad", отправляем "Sad"
    elif voice_emotion == "sadness":
        return "Sad"

    # Если по видео первая эмоция "Surprised", отправляем "Surprised"
    elif video_emotion == "Surprised":
        return "Surprised"

    # Если по видео первая эмоция "Happy", отправляем "Happy"
    elif video_emotion == "Happy":
        return "Happy"

    # Если по голосу первая эмоция "Anger", отправляем "Anger"
    elif voice_emotion == "anger":
        return "Angry"

    elif video_emotion == "nan" and voice_emotion == "nan":
        return "nan"

    elif video_emotion == "nan":
        return voice_emotion

    elif voice_emotion == "nan":
        return video_emotion


async def handle_video_note(message: Message, bot: Bot):
    video_note: VideoNote = message.video_note

    # Получаем информацию о файле
    file_info = await bot.get_file(video_note.file_id)

    # Получаем URL для загрузки файла
    file_path = file_info.file_path

    # Скачиваем файл
    file = await bot.download_file(file_path)

    # Сохраняем файл локально
    video_path = './video/video_note.mp4'
    with open(video_path, 'wb') as new_file:
        new_file.write(file.read())

    # Извлечение аудио из видео и сохранение файлов
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_file_path = './video/video_audio.mp3'
    audio_clip.write_audiofile(audio_file_path)

    video_file_path = './video/video_track.mp4'
    video_clip.write_videofile(video_file_path, codec='libx264', audio=False)

    # Освобождение ресурсов
    audio_clip.close()
    video_clip.close()

    emoV = analyze_video_emotions()
    emoG = analyze_emotion_from_audio()
    final_emotion = determine_final_emotion(emoV, emoG)

    # await bot.send_message(message.from_user.id, f'Ваша эмоция: {final_emotion}')
    return final_emotion


async def handle_video(message: Message, bot: Bot):
    video: Video = message.video

    # Получаем информацию о файле
    file_info = await bot.get_file(video.file_id)

    # Получаем URL для загрузки файла
    file_path = file_info.file_path

    # Скачиваем файл
    file = await bot.download_file(file_path)

    # Сохраняем файл локально
    video_path = './video/video.mp4'
    with open(video_path, 'wb') as new_file:
        new_file.write(file.read())

    # Извлечение аудио из видео и сохранение файлов
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_file_path = './video/video_audio.mp3'
    audio_clip.write_audiofile(audio_file_path)

    video_file_path = './video/video_track.mp4'
    video_clip.write_videofile(video_file_path, codec='libx264', audio=False)

    # Освобождение ресурсов
    audio_clip.close()
    video_clip.close()

    emoV = analyze_video_emotions()
    emoG = analyze_emotion_from_audio()

    final_emotion = determine_final_emotion(emoV, emoG)

    # await bot.send_message(message.from_user.id, f'Ваша эмоция: {final_emotion}')
    return final_emotion


