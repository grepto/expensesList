import json

def maxId(listData):
    """Возвращает максимальный id в списке."""
    tempList = list()
    for item in listData:
        tempList.append(item['id'])
    return max(tempList)

def listItemAdd(listId=3, name='Новый элемент списка', value=0, isCompensated=False, itemId=0):
    fileName = str(listId)+'.json'

    with open('data/'+fileName, 'r+', encoding='utf-8') as f:
        listData = json.load(f)

    newItemId = itemId if itemId != 0 else maxId(listData) + 1
    listData.append(dict(id=newItemId, name=name, value=value, isCompensated=isCompensated))
    resultJson = json.dumps(listData, ensure_ascii=False, indent=2)

    with open('data/' + fileName, 'w', encoding='utf-8') as f:
        f.write(resultJson)

    return

# listItemAdd(3, 'Не очень херовая ручка', 99)


