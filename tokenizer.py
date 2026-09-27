class Tokenizer:
    def __init__(self, text):
        # Разбиваем текст на отдельные слова
        words = text.split()

        # Убираем дубликаты и сортируем
        vocabulary = sorted(set(words))

        # Специальные токены
        self.token_to_id = {
            "<PAD>": 0,
            "<UNK>": 1
        }

        # Добавляем слова в словарь
        for word in vocabulary:
            if word not in self.token_to_id:
                self.token_to_id[word] = len(self.token_to_id)

        # Обратный словарь: число → слово
        self.id_to_token = {
            token_id: token
            for token, token_id in self.token_to_id.items()
        }

    def encode(self, text):
        words = text.split()

        return [
            self.token_to_id.get(word, self.token_to_id["<UNK>"])
            for word in words
        ]

    def decode(self, token_ids):
        return " ".join(
            self.id_to_token.get(token_id, "<UNK>")
            for token_id in token_ids
        )
