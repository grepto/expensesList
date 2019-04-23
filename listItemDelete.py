import json
from _settings import fileDir


def listItemDelete(listId=3, itemId=0):
    """"Удаляет элемент из списка"""
    fileName = fileDir + '.json'

    with open(fileName, 'r', encoding='utf-8') as f:
        listData = json.load(f)

    listData = list(filter(lambda p: p['id'] != itemId, listData))

    resultJson = json.dumps(listData, ensure_ascii=False, indent=2)

    with open(fileName, 'w', encoding='utf-8') as f:
        f.write(resultJson)

    return

# listItemDelete(3, 9)


