import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import os

# 훈련 데이터 이미지 경로
parent_directory = "C:\\Users\\a\\Desktop\\Eng"

# 레이블 지정 (예시입니다. 실제 레이블에 맞게 수정해주세요.)
train_labels = ['same_label']

# 데이터 준비 (ImageDataGenerator 사용)
train_data_gen = ImageDataGenerator(rescale=1./255)
train_data = train_data_gen.flow_from_directory(
    parent_directory,
    classes=train_labels,
    target_size=(128, 128),
    batch_size=3,
    class_mode='categorical'
)

# 간단한 CNN 모델 구축
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(len(train_labels), activation='softmax')
])

# 모델 컴파일
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 모델 훈련
model.fit(train_data, epochs=10)

# 모델 저장 (선택 사항)
model.save('icon_recognition_model.h5')
