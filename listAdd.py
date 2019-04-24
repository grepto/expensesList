import json
from _settings import listsFile
from _common import newId
from listItemAdd import listItemAdd


def listAdd(name, items=None):
    """"Создание нового списка"""

    with open(listsFile, 'r', encoding='utf-8') as f:
        listData = json.load(f)

    newListId = newId(listData)

    listData.append(dict(id=newListId, name=name))
    resultJson = json.dumps(listData, ensure_ascii=False, indent=2)

    with open(listsFile, 'w', encoding='utf-8') as f:
        f.write(resultJson)

    if items is not None:
        for elem in items:
            listItemAdd(newListId, elem['name'], elem['value'], elem['isCompensated'])

    return


items = [{'name': 'СМС-ки', 'value': 99, 'isCompensated': False},
                           {'name': 'Обслуживание счета', 'value': 1990, 'isCompensated': False}]
listAdd('Траты Пихтябрь', items)
