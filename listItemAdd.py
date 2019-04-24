import json
from _settings import fileDir
from _common import newId


def listItemAdd(listId=3, name='Новый элемент списка', value=0, isCompensated=False, itemId=0):
    """Добавляет новый элемент списка

    itemId передается только в том случае, когда функция используется при обновлении существующего элемента списка.
    Если создается новый элемент, параметр itemId не должен передаваться в функцию добавления.
    """
    fileName = fileDir + str(listId)+'.json'

    try:  # Проверяем, существует ли файл строк списка
        with open(fileName, 'r', encoding='utf-8') as f:
            listData = json.load(f)

    except FileNotFoundError:  # Если не существует - создаем
        with open(fileName, 'w', encoding='utf-8') as f:
            listData=list()

    newItemId = itemId if itemId != 0 else newId(listData)
    listData.append(dict(id=newItemId, name=name, value=value, isCompensated=isCompensated))
    resultJson = json.dumps(listData, ensure_ascii=False, indent=2)

    with open(fileName, 'w', encoding='utf-8') as f:
        f.write(resultJson)

    return

# listItemAdd(7, 'Вообще херовая ручка', 99)


