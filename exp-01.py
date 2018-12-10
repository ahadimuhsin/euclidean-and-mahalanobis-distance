import numpy as np
import math

#menghitung euclidean distance
def calc_euclid (x,y):
    euc = 0

    def square (num):
        return math.pow(num,2)

    for i in range (len(x)):
        euc += square(x[i]-y[i])

    return math.sqrt(euc)

#mencari matrix correlation
def correlation (cov, x_, y_, matrix):

    stdx = 0
    stdy = 0

    def square (num):
        return math.pow(num,2)

    def std_dev(num):
        return math.sqrt(num/(len(matrix)-1))

    for i in range (len(matrix)):
        stdx += square(matrix[i][0]-x_)
        stdy += square(matrix[i][1]-y_)

    stdx = std_dev(stdx)
    stdy = std_dev(stdy)

    std = stdx*stdy

    a = cov[0][0]/square(stdx)
    b = cov[0][1]/std
    c = cov[1][0]/std
    d = cov[1][1]/square(stdy)

    return np.array([
        [a, b],
        [c, d]
    ])

def covariance(x, y, x_, y_):
    return (x-float(x_))*(y-float(y_))

'open the file'
file = open ( "F:/Kuliah/Semester 7/Data Mining/Praktikum/1/soal.txt" )
'edit the file location'

'Save the text into array'
x=[]
for line in file.readlines():
    y=[value for value in line.split()] #memisahkan y dengan x
    x.append(y) #menambahkan y ke dalam list
file.close()
print (x)
'save array to a variabel'
matrix = np.array(x).astype(np.float) #save it as float
# print (matrix)

# print(matrix)

'Find Average X and Y'
xSum = 0
ySum = 0
for i in range(len(matrix)):
    xSum += matrix[i][0]
    ySum += matrix[i][1]

xAvg = xSum/len(matrix)
yAvg = ySum/len(matrix)


'covariance'
a = 0
b = 0
c = 0

for i in range (len(matrix)):
    a += covariance(float(x[i][0]), float(x[i][0]), xAvg, xAvg )
    b += covariance(float(x[i][0]), float(x[i][1]), xAvg, yAvg )
    c += covariance(float(x[i][1]), float(x[i][1]), yAvg, yAvg )

a = (a/(len(matrix)))
b = (b/(len(matrix)))
c = (c/(len(matrix)))

cov = np.array ([
    [a, b],
    [b, c]
])

print ('Covariance matrix : ')
print (cov)
print ()
print ('Correlation matrix : ')
print (correlation(cov, xAvg, yAvg, matrix))

# inversing matrix
try:
    inv = np.linalg.inv(cov)
except np.linalg.LinAlgError:
    # Not invertible. Skip this one.
    pass
else:
    # continue with what you were doing
    # print('Matrix inverse : \n', inverse)
    print()
while(True):
    arr = 0
    euclid = 0
    print()
    print('Data 1 :')
    p = float(input('\tFeature no 1 : '))
    q = float(input('\tFeature no 2 : '))
    print('Data 2 : ')
    p1 = float(input('\tFeature no 1 : '))
    q1 = float(input('\tFeature no 2 : '))

    pq = np.array([p, q])
    pq1 = np.array([p1, q1])
    arr = np.subtract(pq, pq1)
    euclid = calc_euclid(pq, pq1)

    print('Euclidean distance   :\n', euclid)
    print('Mahalanobis distance :\n', np.matmul(np.matmul(arr.transpose(), inv), arr))

