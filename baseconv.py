OCTBLOCK = ["000", "001", "010", "011", "100", "101", "110", "111"]
def bin2oct(num, verbose: bool):
    if verbose: print("special: convert {num} from base 2 to base 8:".format(num = num))
    ans = ""; cnt0 = 0
    while len(num) % 3 != 0: cnt0 += 1; num = '0' + num
    if verbose: print("insert {cnt0} more zeroes at the front of the number => {num}".format(cnt0=cnt0, num=num))
    for i in range(0, len(num), 3):
        dig = int(num[i]) * 4 + int(num[i + 1]) * 2 + int(num[i + 2])
        if verbose: print("block 3 digit {bl} convert to digit {dig}".format(bl = num[i:i+3], dig = dig))
        ans += str(dig)
    return ans
def oct2bin(num, verbose):
    if verbose: print("special: convert {num} from base 8 to base 2:".format(num = num))
    ans = ""
    for i in num:
        block = OCTBLOCK[int(i)]; ans += block
        if verbose: print("digit {dig} convert to block 3 digit {bl}".format(bl = block, dig = i))
    return ans

HEXDIG = "0123456789ABCDEF"
HEXBLOCK = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"]
def hexdigit(i):
    return int(i) if i <= '9' else ord(i) - ord('A') + 10
def bin2hex(num, verbose):
    if verbose: print("special: convert {num} from base 2 to base 16:".format(num = num))
    ans = ""; cnt0 = 0
    while len(num) % 4 != 0: num = '0' + num; cnt0 += 1
    if verbose: print("insert {cnt0} more zeroes at the front of the number => {num}".format(cnt0=cnt0, num=num))
    for i in range(0, len(num), 4):
        dig = hexdigit(num[i]) * 8 + hexdigit(num[i + 1]) * 4 + hexdigit(num[i + 2]) * 2 + hexdigit(num[i + 3])
        if verbose: print("block 3 digit {bl} convert to value {val}, which is the digit {dig}".format(bl = num[i:i+4], val = dig, dig = HEXDIG[dig]))
        ans += HEXDIG[dig]
    return ans
def hex2bin(num, verbose):
    if verbose: print("special: convert {num} from base 16 to base 2:".format(num = num))
    ans = ""
    for i in num:
        value = hexdigit(i)
        block = HEXBLOCK[value]
        if verbose: print("digit {dig} which has the value of {value} convert to block 4 digit {bl}".format(bl = block, dig = i, value = value))
        ans += block
    return ans

def toDigList(num):
    ans = []
    for i in num: ans.append(hexdigit(i))
    return ans
def toBase10(num, base, verbose):
    if verbose: print("convert {num} in base {base} to base 10".format(num=num, base = base))
    ans = 0
    num = num[::-1]
    p = 1
    for i in range(len(num)):
        dig = num[i]
        value = dig * p
        if verbose: print("column {col} has digit {dig}, add {value} to answer".format(col = i, dig = dig, value = value))
        ans += value; p *= base
    print("base-10 value: {ans}".format(ans=ans))
    return ans
def b10ToBase(num, base, verbose):
    if verbose: print("convert {num} to base {base}".format(base = base, num = num))
    ans = []
    while num > 0:
        if verbose: print("num / base = quotient {q}, remainder {r}".format(q = num // base, r = num % base))
        ans.append(num % base)
        num //= base
    ans = ans[::-1]
    if verbose: print("reverse the remainders: {ans}".format(ans = ans))
    return ans
def reformat(num):
    ans = ""
    for i in num: ans += HEXDIG[int(i)]
    return ans

if __name__ == "__main__":
    def error():
        print("usage:")
        print()
        print("1. for base conversion: python baseconv.py [original_base] [new_base] [number] (--verbose)")
        print("number in base <= 16 or hexadecimal should be represented with common convention (0123456789ABCDEF)")
        print("otherwise it will be represented as a list of base10-numeral-value digit, seperated by commas.")
        print("use --verbose in order to see how this program works")
        print()
        print("note: please write the [number] input in the correct form mentioned above, i am too lazy to handle all cases possible")
        print()
        print("2. for help: python baseconv.py --help")
        print("or just type python baseconv.py whateveryouwantherewhocares")
        exit(0)

    import sys
    arr = sys.argv[1:]
    if (len(arr) < 3 or len(arr) > 4):
        error()
    baseA, baseB = 0, 0
    num = ""
    try:
        baseA = int(arr[0])
        baseB = int(arr[1])
        num = arr[2]
    except:
        error()

    isVerbose = False
    if len(arr) == 4:
        isVerbose = True
        if arr[3] != "--verbose":
            error()

    if baseA == 2 and baseB == 8: print("answer = {ans}".format(ans = bin2oct(num, isVerbose)))
    elif baseA == 8 and baseB == 2: print("answer = {ans}".format(ans = oct2bin(num, isVerbose)))
    elif baseA == 2 and baseB == 16: print("answer = {ans}".format(ans = bin2hex(num, isVerbose)))
    elif baseA == 16 and baseB == 2: print("answer = {ans}".format(ans = hex2bin(num, isVerbose)))
    else:
        num = toDigList(num)
        num = toBase10(num, baseA, isVerbose)
        num = b10ToBase(num, baseB, isVerbose)
        if baseB <= 16: num = reformat(num)
        print(num)