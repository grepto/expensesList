from listItemDelete import listItemDelete
from listItemAdd import listItemAdd


def listItemUpdate(listId=3, itemId=3, name='Новый элемент списка', value=0, isCompensated=False):
    """"Обновляет элемент списка"""

    listItemDelete(listId, itemId)
    listItemAdd(listId, name, value, isCompensated, itemId)

    return


# listItemUpdate(3, 3, 'Органайзер для проводов IKEA', 899, True)

