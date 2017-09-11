#!/usr/bin/python
# -*- coding: UTF-8 -*-
#author: yoyoyun
#date: 2017/09/11


# 1. 1-1500, 除去2，5，7的倍数，还剩几个数

# 手算思路：
# 为2，5，7的倍数的个数总共有n个，求n。
# （1）2的倍数：1500/2=750个
#     5的倍数：1500/5=300个
#     7的倍数：1500/7（下取整）=214个
#     750+300+214=1264
# （2）2和5的最小公倍数，10的倍数：1500/10=150个
#     2和7的最小公倍数，14的倍数：1500/14=107个
#     5和7的最小公倍数，35的倍数：1500/35=42个
#     去掉（1）中算重复的，1264-150-107-42=965
# （3）2，5和7的最小公倍数，70的倍数：1500/70=21个
#    说明：70在（1）中加了3次，在（2）中减了3次，所以2，5，7的最小公倍数的倍数还需再加上一次
#    n=965+21=986
# 则，还剩1500-n=1500-986=514个。 

# 代码验证结果：
def Num( N ):
    j = 0
    for i in range(1,N+1) :
        if ( i % 2 == 0 ) or ( i % 5 == 0) or ( i % 7 == 0 ) :
            j = j+1
    return N-j

N = 1500
print Num(N)
