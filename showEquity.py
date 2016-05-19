import matplotlib.pyplot as pp
interest=0.03625 # Our interest rate
R=1+interest/365 # Interest multiplier
A=[74504]
M=[12000]
B=[371060]
j=0
while B[j]>0:
  A.append(A[j]*R**15+500-156)
  M.append(M[j]*R**15+750-156)
  B.append(B[j]*R**15-1250+312)
  j+=1
pp.plot(A,color='blue')
pp.plot(M,color='red')
pp.plot(B,color='green')
