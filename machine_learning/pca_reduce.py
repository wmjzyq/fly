#-*- coding: UTF-8 -*-
"""
numpy模拟PCA降维过程
"""

import numpy as np

# 一行为一个样本，一列为一个特征。
A = np.array([[3, 2000],
			  [2, 3000],
			  [4, 5000],
			  [5, 8000],
			  [1, 2000],], dtype='float')

#数据归一化,目的：使特征均值为0
mean = np.mean(A, axis=0)  #求每个特征的均值
"""
[3.e+00 4.e+03]
"""
norm = A - mean            #每个特征减去均值
"""
[[ 0.e+00 -2.e+03]
 [-1.e+00 -1.e+03]
 [ 1.e+00  1.e+03]
 [ 2.e+00  4.e+03]
 [-2.e+00 -2.e+03]]
"""

#数据缩放
scope = np.max(norm,axis=0) - np.min(norm, axis=0)
#[4.e+00 6.e+03]
norm = norm / scope
"""
[[ 0.         -0.33333333]
 [-0.25       -0.16666667]
 [ 0.25        0.16666667]
 [ 0.5         0.66666667]
 [-0.5        -0.33333333]]
"""

#对协方差矩阵进行奇异值分解，求解特征向量
U, S, V = np.linalg.svd(np.dot(norm.T, norm))
"""
[[-0.67710949 -0.73588229]
 [-0.73588229  0.67710949]]
"""
U_reduce = U[:,0].reshape(2,1)
"""
[[-0.67710949]
 [-0.73588229]]
"""
R = np.dot(norm, U_reduce)
print(R)
"""
[[ 0.2452941 ]
 [ 0.29192442]
 [-0.29192442]
 [-0.82914294]
 [ 0.58384884]]
"""



"""
恢复过程
"""
Z = np.dot(R, U_reduce.T)
print(Z)
A_resume = np.multiply(Z, scope) + mean
print(A_resume)
#恢复后的数据有失真