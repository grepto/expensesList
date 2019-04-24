import json
import os
from _settings import listsFile, fileDir, commonResult


def listDelete(listId = -1):
    """Удаление списка"""

    fileName = fileDir + str(listId)+'.json'
    result = commonResult

    with open(listsFile, 'r', encoding='utf-8') as f:
        listData = json.load(f)

    isListExists = len(list(filter(lambda p: p['id'] == listId, listData))) > 0
    if isListExists:
        listData = list(filter(lambda p: p['id'] != listId, listData))
        resultJson = json.dumps(listData, ensure_ascii=False, indent=2)

        with open(listsFile, 'w', encoding='utf-8') as f:
            f.write(resultJson)

        """Удаление файла с содержимым удаляемого списка"""
        if os.path.exists(fileName):
            os.remove(fileName)
    else:
        result = dict(isError=True, errorText=f'list id {listId} does not exists')

    return result

# print(listDelete(4))
