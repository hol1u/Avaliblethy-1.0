from tokenizer import Tokenizer


# Загружаем наш текст
with open("data.txt", "r", encoding="utf-8") as file:
    text = file.read()


# Создаём tokenizer
tokenizer = Tokenizer(text)


# Показываем словарь
print("Vocabulary:")
print(tokenizer.token_to_id)

print()


# Проверяем encode
sentence = "hello world"

tokens = tokenizer.encode(sentence)

print("Text:")
print(sentence)

print()

print("Token IDs:")
print(tokens)

print()


# Проверяем decode
decoded = tokenizer.decode(tokens)

print("Decoded:")
print(decoded)
