# -*- coding: utf-8 -*-

import numpy as np

array = np.array([1,2,3,4,5,6,7,8]) # 1*4 vektor
print("shape:" , array.shape) #shape

a= array.reshape(2,4)
print(a)
print("shape:" , a.shape) 
print("dimension:" , a.ndim) #dimension
print("data type:" , a.dtype.name) #data type
print("size:" , a.size) #data type
print("type" , type(a)) #array type

array1 = np.array([[1,2,3],[1,2,3],[1,2,3]]) # 3*3 vektor
print(array1)
print("shape:" , array1.shape) 

print(np.zeros((3,3))) #zero array -- allocate array
print(np.ones((3,3))) #one array

array1[0,0] = 5
print(array1)

print(np.empty((2,3))) #empty array

b= np.arange(10,50,5).reshape(2,4) #10 50 arası beşer beşer arraya koyar
print(b)

c= np.linspace(10,50,20).reshape(4,5)
print(c)

#%%

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b) #toplama
print(a-b) #çıkarma
print(a*b) #çarpma
print(a**b) #karesi

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2,3],[4,5,6]])

print(a*b) #çarpma
print(a.dot(b.T)) #transpoze çarpım
print(np.exp(a)) #exp


c= np.random.random((5,5)) #random
print(c)
print(c.sum()) #toplam tüm elemanları
print(c.sum(axis=0)) #toplam satır
print(c.sum(axis=1)) #toplam sütun
print(c.max()) #max eleman
print(c.min()) #min eleman
print(np.sqrt(c)) #kök
print(np.square(c)) #kare
print(np.add(c,c)) #ekleme
print(c+c) #iki matris toplam

#%%

array= np.array([1,2,3,4,5,6,7])

print(array[0])
print(array[:4])

reverse_array = array[::-1]
print(reverse_array)

array2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array2)
print(array2[1][1])
print(array2[:,1])
print(array2[1,1:4])
print(array2[-1,:])


#%%

array = np.array([[1,2,3],[4,5,6],[7,8,9]])

a = array.ravel()
print(a)

array2 = a.reshape(3,3) #yeni parametreye size işlemi yapılır
print(array2)

arrayT = array2.T
print(arrayT)


a.resize((3,3)) #kendisine size işlemi yapılır
print(a)

#%%

array1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
array2 = np.array([[-1,-2,-3],[-4,-5,-6],[-7,-8,-9]])

array3 = np.vstack((array1,array2)) #vertical birleşim
array4 = np.hstack((array1,array2)) #horizantal birleşim
print(array3)
print(array4)


#%%

liste = [1,2,3,4]
array = np.array(liste)
print(array )
print(type(array))

liste2 = list(array)
print(liste2)
print(type(liste2))

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = a
c = b

b[0][0] = 5
print(b)
print(a)
print(c)

d = np.array([[1,2,3],[4,5,6],[7,8,9]])
e = d.copy()
f = d.copy()
e[0][0] = 5
print(d)
print(e)
print(f)



