class Historia():
    def __init__(self, title, text, type_words):
        self.__title = title
        self.__text = text
        self.__user_words = []
        self.__type_words = type_words
        self.__text_complete = ''

    def complete_text(self):
        self.__text_complete = self.__text
        for word in self.__user_words:
            self.__text_complete = self.__text_complete.replace("*", word, 1)

        print(self.__text_complete)

    def ask(self):
        for word in self.__type_words:
            user_word = input(f'Dame un(a) {word}: ')

            while not len(user_word.strip()):
                user_word = input(f'Dame un(a) {word}: ')

            self.__user_words.append(user_word)
