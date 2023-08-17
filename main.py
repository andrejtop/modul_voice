import whisper

def speech_to_text(model='base'):# base, small, medium, large, xlarge
    speech_model = whisper.load_model(model)# подгружаем модель
    result = speech_model.transcribe('C:/Users/User/download/track123.mp3')# распознаём текст

    with open('text.txt', 'w', encoding='utf-8') as file:
        file.write(result['text'])# в result приходит большой словарь с данными.
        # Нам нужен ключ text, в котором и находится распознанный текст.

def main():
    models = {1: 'base', 2: 'small', 3: 'medium', 4: 'large', 5: 'xlarge'}
    for key, value in models.items():
        print(f'{key}: {value}')

    model = int(input('Введите номер модели (цифра от 1 до 5): '))
    if model not in models.keys():
        raise KeyError('Такая модель не существует')
    print('Запущен процесс распознавания текста, ожидайте...')
    speech_to_text(model=models[model])



if __name__ == '__main__':
    main()



