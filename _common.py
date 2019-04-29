"""Общие функции"""


def newId(listData):
    """Возвращает id который нужно присвоить следующему элементу."""
    try:
        tempList = list()
        for item in listData:
            tempList.append(item['id'])
        return max(tempList) + 1
    except ValueError:
        return 0


