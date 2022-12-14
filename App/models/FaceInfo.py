class FaceInfo:
    __id = 0
    __name = ''

    def __init__(self, id, name):
        __id = id
        __name = name

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name
