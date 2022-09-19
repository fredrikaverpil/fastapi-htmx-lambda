from emoji_translate.emoji_translate import Translator as EmojiTranslator
from googletrans import Translator as GoogleTranslator

emo = EmojiTranslator(exact_match_only=False, randomize=True)
google_translator = GoogleTranslator()


def get_translation(text: str, target_lang: str = "en") -> str:
    translated_text = google_translator.translate(text, dest=target_lang).text
    return translated_text


def get_result(myquery: str) -> str:

    if "+" in myquery:
        array = myquery.split("+")
        return str(sum([int(i) for i in array]))
    elif "-" in myquery:
        array = myquery.split("-")
        return str(int(array[0]) - int(array[1]))
    elif "/" in myquery:
        array = myquery.split("/")
        return str(float(array[0]) / float(array[1]))
    elif "*" in myquery:
        array = myquery.split("*")
        return str(float(array[0]) * float(array[1]))

    elif "korv" in myquery.lower():
        return "🌭"
    elif "katt" in myquery.lower():
        return "🐱"
    elif "hund" in myquery.lower():
        return "🐶"

    else:
        translation = get_translation(myquery)
        return emo.emojify(translation)
