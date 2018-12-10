import math

def S_x(i, j, d, mat, mis):
    return (i+j)*mat/2 - d*(mat-mis)

def main(a,b):
    M = len(a) - 1
    N = len(b) - 1
    mat = 2
    mis = -1
    ind = -2
    X = 2
    T_x, T, i = 0,0,0
    mx = max(M,N)
    R = [[-math.inf for w in range(mx+1)] for q in range(mx+1)]
    for x in range(mx):
        for y in range(mx):
            R[x][y] = -math.inf
    T = [-math.inf for q in range(mx+1)]
    while (i<min(M, N)) and a[i] == b[i]:
        i+=1
    R[0][0] = i
    T_x = S_x(i,i,0, mat, mis)
    T[0] = T_x
    d = 0
    L = 0
    U = 0
    while L < U + 2:
        print(1)
        d+=1
        d_x = int(max((d - math.floor((X + mat / 2) / (mat - mis)) - 1), 0))
        for k in range(max(0,L-1),U+1):
            print(2)
            firstI = -math.inf
            secondI = -math.inf
            thirdI = -math.inf
            if L < k:
                firstI = R[d-1][k-1] + 1
            if (L <= k) and (k <= U):
                secondI = R[d - 1][k] + 1
            if k < U:
                thirdI = R[d-1][k+1]
            i = max(firstI, secondI,thirdI)
            j = i - k
            if (i > -math.inf) and (S_x(i, j, d, mat, mis) >= (T[d_x] - X)):
                while (i < (M)) and (j<(N)) and (a[i+1] == b[j+1]):
                    i += 1
                    j += 1
                R[d][k] = i
                T_x = max(T_x, S_x(i, j, d, mat, mis))
            else:
                R[d][k] = -math.inf
        T[d] = T_x
        for k in range(mx):
            if R[d][k] > -math.inf:
                L = k
                break
        p = mx
        for k in range(mx):
            p -= 1
            if R[d][p] > -math.inf:
                U = k
                break
        for k in range(mx):
            p -= 1
            if R[d][p] == N + k:
                L = k
                break
        for k in range(mx):
            if R[d][k] > -math.inf:
                U = min(U, k - 2)
                break

    return T_x


