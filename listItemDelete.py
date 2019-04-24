import json
from _settings import fileDir, commonResult


def listItemDelete(listId=3, itemId=0):
    """"Удаляет элемент из списка"""
    fileName = fileDir + str(listId)+'.json'
    result = commonResult

    with open(fileName, 'r', encoding='utf-8') as f:
        listData = json.load(f)

    isItemExists = len(list(filter(lambda p: p['id'] == itemId, listData))) > 0
    if isItemExists:
        listData = list(filter(lambda p: p['id'] != itemId, listData))

        resultJson = json.dumps(listData, ensure_ascii=False, indent=2)

        with open(fileName, 'w', encoding='utf-8') as f:
            f.write(resultJson)

    else:
        result = dict(isError=True, errorText=f'item id {itemId} does not exists in list id {listId}')

    return result

# print(listItemDelete(3, 99))


