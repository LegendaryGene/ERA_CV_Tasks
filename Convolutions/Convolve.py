import numpy as np
a=np.array([[1,0,1,0,1],
            [0,1,1,1,0],
            [1,1,1,1,1],
            [0,1,1,1,0],
            [1,0,1,0,1]])
b=np.array([[0,1,0],
            [1,1,1],
            [0,1,0]])
ans=np.array([])
for x in range(a.shape[0]-b.shape[0]+1):
    for y in range(a.shape[0]-b.shape[0]+1):
        sum=0
        for i in range(b.shape[0]):
            for j in range(b.shape[1]):
                sum+=a[i+x,j+y]*b[i,j]
        ans=np.append(ans,sum)
ans=np.reshape(ans,(a.shape[0]-b.shape[0]+1,a.shape[0]-b.shape[0]+1))
print(ans) 