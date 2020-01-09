import public.Comment as comments
import public.Scan as scans
import argparse

def pmian():
    print('''
    --
    |       MIMAZ.ORG  CodeFileSCAN  V1.0
            2020 - CMS - FAMILY            |
                                          --
    ''')

def uinput():
    parser = argparse.ArgumentParser(description="CodeFileSCAN  V1.0")
    parser.add_argument("-f", type=str, required=True, help="must need route like: test , do not need \.")
    return parser.parse_args()

def main():
    route = args.f
    X1 = comments.comment('testone')
    X2 = scans.MimazScan('testone')
    #文件原始数组
    FileDic = X1.GetFileAndRoute(route)
    #文件一维数组
    FinArray = []
    for k,v in FileDic.items():
        FinArray.extend(X2.FileScan(k,v))
    #检测数组
    checkArray = ['password=','password:','key=','key:']
    #结果数组
    ResArray = []
    for eFinArray in FinArray:
        #单次扫面结果集
        eresarray = X2.HeartScan(eFinArray, checkArray)
        for eeresarray in eresarray:
            if len(eeresarray[0]) > 0:
                ResArray.append(eeresarray)
    for eResArray in ResArray:
        print('文件位置：{} 代码行数：{} 触发规则：{}'.format(eResArray[0], eResArray[1], eResArray[2]))

if __name__ == "__main__":
    args = uinput()
    main()
