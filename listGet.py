import json
from _settings import listsFile, fileDir, commonResult
from _common import error

def listGet(listId = 3):
    """"Возвращает JSON модель списка. В начале идут атрибуты списка, затем массив элементов."""

    fileName = fileDir + str(listId)+'.json'
    result = commonResult

    with open(listsFile, 'r', encoding='utf-8') as f:
        listHead = list(filter(lambda p: p['id'] == listId, json.load(f)))

    try:
        with open(fileName, 'r', encoding='utf-8') as f:
            listContent = sorted(json.load(f), key=lambda k: k['id'])
    except FileNotFoundError:
        listContent = list()

    totalValue = sum(elem['value'] for elem in listContent)

    if len(listHead) > 0:
        resultList = dict(id=listId, name=listHead[0]['name'], totalValue=totalValue, lines=listContent)
        result.update(resultList)
    else:
        result = error(1, listId)

    # resultJson = json.dumps(result, ensure_ascii=False, indent=2)

    return result


# print(listGet(5))
