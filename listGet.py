import json

def listGet(listId = 3):
    with open('data/lists.json', 'r', encoding='utf-8') as f:  # открываем файл на чтение
        listHead = json.load(f)  # загружаем из файла данные в словарь settings

    with open ('data/'+str(listId)+'.json', 'r', encoding='utf-8') as f:
        listData = json.load(f)

    listData = sorted(listData, key=lambda k: k['id'])

    listResult = dict(id=listId, name=listHead[listId]['name'])
    listResult['lines'] = listData

    resultJson = json.dumps(listResult, ensure_ascii=False, indent=2)

    return resultJson


# print(listGet())

