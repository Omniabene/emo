import cv2
import numpy as np
from keras.models import model_from_json


def analyze_video_emotions():
    emotion_dict = {
        0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"
    }
    emotions_of_interest = ["Angry", "Happy", "Sad", "Surprised", "Fearful"]

    video_path = "C:\\Users\\NikitaPC\\PycharmProjects\\pythonProject\\video\\video_track.mp4"

    # Загрузка архитектуры модели из JSON файла
    json_file = open('model/emotion_model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    emotion_model = model_from_json(loaded_model_json)

    # Загрузка весов модели
    emotion_model.load_weights("model/emotion_model.h5")
    print("Модель загружена из файла")

    cap = cv2.VideoCapture(video_path)

    total_frames = 0
    total_emotion_percentages = np.zeros(7)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Преобразование кадра в массив numpy и добавление размерности батча
        img_array = cv2.resize(frame, (224, 224))
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0  # Масштабирование значений пикселей в диапазоне [0, 1]

        # Предсказание эмоции
        emotion_prediction = emotion_model.predict(img_array)

        emotion_percentages = emotion_prediction[0] * 100
        total_emotion_percentages += emotion_percentages
        total_frames += 1

    cap.release()

    average_emotion_percentages = total_emotion_percentages / total_frames
    emotion_result = dict(zip(emotion_dict.values(), average_emotion_percentages))

    filtered_emotions = {key: emotion_result[key] for key in emotions_of_interest}
    sorted_emotions = sorted(filtered_emotions.items(), key=lambda x: x[1], reverse=True)

    # Возвращение отсортированных эмоций
    if np.isnan(sorted_emotions[0][1]):
        return "nan"
    else:
        return sorted_emotions[0][0]


# Пример использования:

# emotions = analyze_video_emotions()
# print(emotions)