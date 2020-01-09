import os

class comment:
    def __init__(self, id):
        self.projectid = id
    def GetFileAndRoute(self, route):
        FileDic = {}
        for i,_,k in os.walk(route):
            if len(k) > 0:
                FileDic[i] = k
        return FileDic