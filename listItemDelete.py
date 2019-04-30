import json
from _settings import fileDir, commonResult
from _common import error


def listItemDelete(listId=3, itemId=0):
    """"Удаляет элемент из списка"""
    fileName = fileDir + str(listId)+'.json'
    result = commonResult

    try:
        """Открываем файл строк списка"""
        with open(fileName, 'r', encoding='utf-8') as f:
            listData = json.load(f)

    except FileNotFoundError:
        """Если нет файла строк списка - значит нет и самого списка"""
        result = error(1, listId)

    else:
        isItemExists = len(list(filter(lambda p: p['id'] == itemId, listData))) > 0
        if isItemExists:
            listData = list(filter(lambda p: p['id'] != itemId, listData))

            resultJson = json.dumps(listData, ensure_ascii=False, indent=2)

            with open(fileName, 'w', encoding='utf-8') as f:
                f.write(resultJson)
        else:
            result = error(2, itemId, listId)

    return result

# print(listItemDelete(55, 1))

