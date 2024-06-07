from translate import Translator

class Transl:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def translate(self, txt):
        translator = Translator(from_lang=self.first, to_lang=self.second)

        return translator.translate(txt)