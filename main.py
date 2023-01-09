class TreeStore:
    def __init__(self, items):
        self.items = items

    def getAll(self):
        return self.items

    def getItem(self, id):
        for item in self.items:
            if item['id'] == id:
                return item

    def getChildren(self, id):
        return [item for item in self.items if item['parent'] == id]

    def getAllParents(self, id):
        parent_id: int | str = id
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
