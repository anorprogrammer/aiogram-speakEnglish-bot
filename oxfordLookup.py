import requests

app_id = "77568e5b"
app_key = "4abb83f9736938fb4010d4f5a6a78dda"
language = "en-gb"

def getDifinitions(word_id):
    url = 'https://od-api.oxforddictionaries.com/api/v2/entries/' + language + '/' + word_id
    r = requests.get(url=url, headers = {'app_id' : app_id, 'app_key' : app_key})
    res = r.json()

    if 'error' in res.keys():
        return False

    output = {}
    senses = res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definitions = []
    for sense in senses:
        definitions.append(f"👉 {sense['definitions'][0]}")
    output['definitions']="\n".join(definitions)

    if res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
        output['audio'] = res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']

    return output


if __name__ == '__main__':
    from pprint import pprint as print
    print(getDifinitions("Great"))

