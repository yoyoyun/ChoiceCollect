# ChoiceCollect
## 1. 1-1500, 除去2，5，7的倍数，还剩几个数
思路：为2，5，7的倍数的个数总共有n个，求n。</br>
（1）2的倍数：1500/2=750个</br>
     5的倍数：1500/5=300个</br>
     7的倍数：1500/7（下取整）=214个</br>
     750+300+214=1264</br>
（2）2和5的最小公倍数，10的倍数：1500/10=15个</br>
     2和7的最小公倍数，14的倍数：1500/14=107个</br>
     5和7的最小公倍数，35的倍数：1500/35=42个</br>
     去掉（1）中算重复的，1264-15-107-42=1100</br>
（3）2，5和7的最小公倍数，70的倍数：1500/70=21个</br>
    说明：70在（1）中加了3次，在（2）中减了3次，所以2，5，7的最小公倍数的倍数还需再加上一次</br>
    n=1100+21=1121</br>
则，还剩1500-n=1500-1121=379个。</br>
