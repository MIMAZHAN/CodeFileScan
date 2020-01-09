# CodeFileScan
### 代码敏感信息扫描

#### 说明：  

-f 指定项目地址   
例如：index.py -f test

#### 其他：
  
* index.py中，main()函数：checkArray为检测数组，您可以定义检测关键字，请不要带空格。  
* public/Scan.py中，该行：#wArray.append(eeline)可以记录目标原始代码，结果有些代码很长，导致结果输出很难看，现注释掉。

#### TODO：

优化扫描检测数组checkArray，优化扫描实现。

#### 题外：
早有大佬已经实现，这里只是最基础的实现，代码简单易懂。
