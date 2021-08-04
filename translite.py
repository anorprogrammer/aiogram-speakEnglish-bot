from googletrans import Translator

translator =Translator()

def tarjimon(message):
    transdict={}
    lang = translator.detect(message).lang
    transdict["lang"] =lang
    dest = "uz" if lang=="en" else "en"
    transdict["result"]=translator.translate(message, dest).text
    return transdict

if __name__ == '__main__':
    print(tarjimon("Osmon"))