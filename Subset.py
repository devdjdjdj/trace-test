import sys

def to_string(B):
    result = []
    for i in range(1, len(B)):
        if B[i] == 1:
            result.append(str(i))
    return "{"+", ".join(result)+"}"

def removeLast(B):
    l = len(B)
    for i in range(len(B)-1,0,-1):
        if B[i] == 1:
            B[i] = 0
            break

def printSubsets(B,k,i):
    if k <= 0:
        print(to_string(B))
        return

    for j in range(i, len(B)):
        B[j] = 1
        printSubsets(B, k-1, j+1)
        removeLast(B)

def init_B(N):
    result = [99]
    for i in range(N):
        result.append(0)
    return result

if __name__ == '__main__':
    try:
        n = int(sys.argv[1])
        k = int(sys.argv[2])
        B = init_B(n)
        printSubsets(B,k,1)
    except:
        print()
