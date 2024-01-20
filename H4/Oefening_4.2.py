import numpy as np

m1 = np.array(([3,8,5],[4,6,3],[2,5,-3]))
m2 = np.array(([7,0,8],[4,-9,6],[1,6,4]))

m3 = m1+m2
print(m3)

m4 = m1*2
print(m4)

m5 = m1*m2
print(m5)

m6 = np.dot(m1,m2)
print(m6)

m7 = np.transpose(m2)
print(m7)

m8i = m1[[1,0,2],:]
print(m8i)

m8ii = m2[:, [2,1,0]]
print(m8ii)