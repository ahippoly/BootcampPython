import sys

arg = sys.argv
arg_count = len(arg)
res = ""

for i in range(1, arg_count - 1):
    res += arg[i] + " "
if arg_count > 1 :
    res += arg[arg_count - 1]
    print(res[::-1].swapcase())
