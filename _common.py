"""Общие функции"""


def maxId(listData):
    """Возвращает максимальный id в списке."""
    try:
        tempList = list()
        for item in listData:
            tempList.append(item['id'])
        return max(tempList)
    except ValueError:
        return 0


