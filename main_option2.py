class TreeStore:
    def __init__(self, items):
        temp = {}
        for item in items:
            temp[item['id']] = item

        self.items = temp

    def getAll(self):
        result = []
        for item in self.items.values():
            result.append(item)
        return result

    def getItem(self, id):
        return self.items[id]

    def getChildren(self, id):
        return [item for item in self.items.values() if item['parent'] == id]

    def getAllParents(self, id):
        parent_id: int|str = id  #начальный parent_id равен id начального элемента, чтобы включить его в родительскую цепочку
        result = []

        while parent_id != 'root':
            temp = self.getItem(parent_id)
            parent_id = temp['parent']
            result.append(temp)

        return result


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]

ts = TreeStore(items)

# print(ts.getAll())
# print(ts.getItem(7))
# print(ts.getChildren(4))
# print(ts.getAllParents(7))
