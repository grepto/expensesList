from listItemDelete import listItemDelete
from listItemAdd import listItemAdd


def listItemUpdate(listId=3, itemId=3, name='Новый элемент списка', value=0, isCompensated=False):
    """"Обновляет элемент списка"""

    result = listItemDelete(listId, itemId)

    if result['isError'] is False:
        result = listItemAdd(listId, name, value, isCompensated, itemId)

    return result


# print(listItemUpdate(3, 33, 'Органайзер для проводов IKEA', 899, True))

