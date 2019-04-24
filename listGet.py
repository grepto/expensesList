import json
from functools import reduce
from _settings import listsFile, fileDir

def listGet(listId = 3):
    """"Возвращает JSON модель списка. В начале идут атрибуты списка, затем массив элементов."""

    fileName = fileDir + str(listId)+'.json'

    with open(listsFile, 'r', encoding='utf-8') as f:
        listHead = json.load(f)

    try:
        with open(fileName, 'r', encoding='utf-8') as f:
            listData = json.load(f)
    except FileNotFoundError:
        listData = list()


    try:
        listResult = dict(id=listId, name=listHead[listId]['name'])
    except:
        listResult = dict()

    totalValue = sum(elem['value'] for elem in listData)
    listResult['totalValue'] = totalValue

    listData = sorted(listData, key=lambda k: k['id'])
    listResult['lines'] = listData

    resultJson = json.dumps(listResult, ensure_ascii=False, indent=2)

    return resultJson


print(listGet(3))

