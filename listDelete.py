import json
import os
from _settings import listsFile, fileDir


def listDelete(listId = -1):
    """Удаление списка"""

    fileName = fileDir + str(listId)+'.json'
    if os.path.exists(fileName):
        print(fileName)
        os.remove(fileName)

    with open(listsFile, 'r', encoding='utf-8') as f:
        listData = json.load(f)

    listData = list(filter(lambda p: p['id'] != listId, listData))

    resultJson = json.dumps(listData, ensure_ascii=False, indent=2)

    with open(listsFile, 'w', encoding='utf-8') as f:
        f.write(resultJson)

    return

# listDelete(99)
