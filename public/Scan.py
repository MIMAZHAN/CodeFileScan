import re

class MimazScan:
    def __init__(self, id):
        self.projectid = id
    def FileScan(self, route, fileArray):
        FinallyRoute = []
        if route[:-1].endswith('\\'):
            pass
        else:
            route = route+'\\'
        for everyfile in fileArray:
            FinallyRoute.append(route + everyfile)
        return FinallyRoute
    def HeartScan(self, route, checkArray):
        route = route.replace('\\\\','\\')
        with open(route, mode='r', errors='ignore', encoding='utf-8') as fObject:
            rline = fObject.read().split("\n")
            count = 1
            reArray = []
        for eline in rline:
            #eeline = eline
            eline = eline.replace(' ','')
            for ecArray in checkArray:
                if re.search(ecArray, eline, re.IGNORECASE):
                    wArray = []
                    wArray.append(route)
                    wArray.append(count)
                    #wArray.append(eeline)
                    wArray.append(ecArray)
                    reArray.append(wArray)
            count += 1
        return reArray


        