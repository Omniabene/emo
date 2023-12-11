# from rich import print
# import torch
# from aniemore.recognizers.voice import VoiceRecognizer
# from aniemore.models import HuggingFaceModel
# from pathlib import Path
# import warnings
# import librosa


# def analyze_emotion_from_audio():
#     audio_file_path = Path("C:\\Users\\NikitaPC\\PycharmProjects\\pythonProject\\video\\video_audio.mp3")
#
#     audio_data, sr = librosa.load(audio_file_path)
#
#     mean_amplitude = sum(abs(audio_data)) / len(audio_data)
#
#     print(mean_amplitude)
#
#     threshold = 0.001
#     if mean_amplitude <= threshold:
#         return "nan"
#
#     model = HuggingFaceModel.Voice.WavLM
#     device = 'cuda' if torch.cuda.is_available() else 'cpu'
#
#     vr = VoiceRecognizer(model, device)
#     result = vr.recognize(str(audio_file_path))
#
#     # Оставим только нужные эмоции
#     filtered_emotions = {
#         'anger': result.get('anger', 0),
#         'happiness': result.get('happiness', 0),
#         'sadness': result.get('sadness', 0),
#         'neutral': result.get('neutral', 0)
#     }
#
#     # Сортируем по убыванию значений
#     sorted_emotions = dict(sorted(filtered_emotions.items(), key=lambda item: item[1], reverse=True))
#
#     emotions = ['anger', 'happiness', 'sadness', 'neutral']
#     max_emo_name = ''
#     max_emo = -1
#     for emo in sorted_emotions:
#         if sorted_emotions[emo] > max_emo and emo in emotions:
#             max_emo = sorted_emotions[emo]
#             max_emo_name = emo
#     return max_emo_name
#
# # print(analyze_emotion_from_audio())

from voiceUtils.ddatasets import load_dataset
from voiceUtils.transformors import AutoProcessor, AutoModel, fit
import torch
from aniemore.recognizers.voice import VoiceRecognizer
from aniemore.models import HuggingFaceModel
from pathlib import Path


def analyze_emotion_from_audio():
    # загружаем обученную модель
    processor = AutoProcessor.from_pretrained("Aniemore/wav2vec2-xlsr-53-russian-emotion-recognition",
                                              trust_remote_code=True)
    modell = AutoModel.from_pretrained("Aniemore/wav2vec2-xlsr-53-russian-emotion-recognition",
                                       trust_remote_code=True)

    # загружаем датасет от сбера с русскими голосами
    dataset = load_dataset("Aniemore/bond005/wav2vec2-large-ru-golos-with-lm ")

    emotions = ['anger', 'happiness', 'sadness', 'neutral']
    fit(modell, dataset, classes=emotions)

    voice_file_path = Path("C:\\Users\\NikitaPC\\PycharmProjects\\pythonProject\\video\\video_audio.mp3")

    model = HuggingFaceModel.Voice.WavLM

    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    vr = VoiceRecognizer(model, device)
    result = vr.recognize(str(voice_file_path))

    emotions = ['anger', 'happiness', 'sadness', 'neutral']
    max_emo_name = ''
    max_emo = -1
    for emo in result:
        if result[emo] > max_emo and emo in emotions:
            max_emo = result[emo]
            max_emo_name = emo
    return max_emo_name

# print(analyze_emotion_from_audio())
