import numpy as np

def smith_waterman(a, b, align_score = 2, gap = 1):
    H = np.zeros((len(a) + 1, len(b) + 1))
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            match = H[i-1,j-1] + (align_score if a[i-1] == b[j-1] else 0)
            delete = H[1:i,j].max() - gap if i > 1 else 0
            insert = H[i,1:j].max() - 2*gap if j > 1 else 0
            H[i,j] = max(match, delete, insert, 0)
    return H.max()





