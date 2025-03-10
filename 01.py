# 1.使用tensorflow2.0完成以下操作（每小题10分）
import tensorflow as tf
# (1)矩阵创建
# ①创建一个维度为3*3的全1矩阵
tf_ones = tf.ones(shape=[3, 3])
# ②使用range，创建一个1-9的1阶张量
tf_range = tf.range(1, 10)
# ③打印上题的维度
print(tf_range.shape)
# ④将上题维度修改为3,1,3
tf_reshape = tf.reshape(tf_range, shape=[3, 1, 3])
# ⑤使用函数，去除维度中函数1的维度
tf_squeeze = tf.squeeze(tf_reshape)
# (2)切片及其他
# ①使用1-9的向量，使用切片，打印3,4,5,6  1，2，3，4，5，6，7，8，9 a[2:5]
tf_range1 = tf_range[2:6]
print(tf_range1)
# ②打印上题向量的均值
print(tf.reduce_mean(tf_range1))
# ③创见一个2行2列的标准正态分布矩阵
tf_random_normal = tf.random.normal(shape=(2, 2))
# ④创建一个2行2列的全0矩阵
tf_zeros = tf.zeros(shape=(2, 2))
# ⑤将3,4问的结果拼接成一个4行2列的结果
tf_concat = tf.concat([tf_random_normal, tf_zeros], axis=0)
print(tf_concat)