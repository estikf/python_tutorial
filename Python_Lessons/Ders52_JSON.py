import json

with open('data.json', 'r') as f:
    content = json.load(f)

    # json.load(f) koduyla içeriği content stringine atıyoruz.

    for friend in content['friends']:
        del friend['age']
    print(content)

with open('data.json', 'r') as f, open('data2.json', 'w') as f2:
    json.dump(content, f2)
