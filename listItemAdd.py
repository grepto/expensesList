import json
from _settings import fileDir, commonResult, listsFile
from _common import newId, error


def listItemAdd(listId=3, name='Новый элемент списка', value=0, isCompensated=False, itemId=0):
    """Добавляет новый элемент списка

    itemId передается только в том случае, когда функция используется при обновлении существующего элемента списка.
    Если создается новый элемент, параметр itemId не должен передаваться в функцию добавления.
    """
    fileName = fileDir + str(listId)+'.json'
    result = commonResult.copy()

    with open(listsFile, 'r', encoding='utf-8') as f:
        listHead = list(filter(lambda p: p['id'] == listId, json.load(f)))

    if len(listHead) > 0:
        try:  # Проверяем, существует ли файл строк списка
            with open(fileName, 'r', encoding='utf-8') as f:
                listData = json.load(f)

        except FileNotFoundError:  # Если не существует - создаем
            with open(fileName, 'w', encoding='utf-8') as f:
                listData=list()

        newItemId = itemId if itemId != 0 else newId(listData)
        newItem = dict(id=newItemId, name=name, value=value, isCompensated=isCompensated)

        listData.append(newItem)
        resultJson = json.dumps(listData, ensure_ascii=False, indent=2)

        with open(fileName, 'w', encoding='utf-8') as f:
            f.write(resultJson)

        result.update(newItem)

    else:
        result = error(1, listId)

    return result

# print(listItemAdd(3, 'Вообще херовая ручка', 99))


