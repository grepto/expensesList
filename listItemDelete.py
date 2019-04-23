import json


def listItemDelete(listId=3, itemId=0):
    fileName = str(listId) + '.json'
    with open('data/'+fileName, 'r', encoding='utf-8') as f:
        listData = json.load(f)

    listData = list(filter(lambda p: p['id'] != itemId, listData))

    resultJson = json.dumps(listData, ensure_ascii=False, indent=2)

    with open('data/' + fileName, 'w', encoding='utf-8') as f:
        f.write(resultJson)

listItemDelete(3, 5)


