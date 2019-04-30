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


def error(errCode, *errVariables):
    """Возвращает объект ошибки"""

    errors = {
        -1: {'template': 'not enough errVarialbes. Expected {}'},
        1: {'template': 'list id {} does not exists', 'errVariables': 'listId'},
        2: {'template': 'item id {} does not exists in list id {}', 'errVariables': 'itemId, listId'}
    }
    template = errors[errCode]['template']

    try:
        errorText = template.format(*errVariables)
    except IndexError:
        expectedVariables = errors[errCode]['errVariables']
        return error(-1, expectedVariables)

    return {'isError': True, 'errorText': errorText, 'errorCode': errCode}

