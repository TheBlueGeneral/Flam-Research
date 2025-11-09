import math, numpy as np, pandas as pd

df=pd.read_csv("xy_data.csv")
x=df["x"].to_numpy();y=df["y"].to_numpy()
t=np.linspace(6,60,len(df))

def f(t,a,m,x0):
 c=np.cos(a);s=np.sin(a)
 u=np.exp(m*np.abs(t))*np.sin(0.3*t)
 x=t*c-u*s+x0
 y=42+t*s+u*c
 return x,y

def best(a,m):
 c=np.cos(a);s=np.sin(a)
 u=np.exp(m*np.abs(t))*np.sin(0.3*t)
 x0=t*c-u*s
 X=float(np.mean(x-x0))
 xp,yp=f(t,a,m,X)
 L=np.mean((xp-x)**2+(yp-y)**2)
 return L,X

bestL=1e18;A=None;M=None;X=None

for th in np.linspace(0.5,49.5,200):
 a=math.radians(th)
 for m in np.linspace(-0.05,0.05,200):
  L,x0=best(a,m)
  if L<bestL:
   bestL=L;A=th;M=m;X=x0

for th in np.linspace(A-2,A+2,1200):
 a=math.radians(th)
 for m in np.linspace(-0.0499,-0.03,600):
  L,x0=best(a,m)
  if L<bestL:
   bestL=L;A=th;M=m;X=x0

a=math.radians(A)
xp,yp=f(t,a,M,X)
rmse=float(np.sqrt(np.mean((xp-x)**2+(yp-y)**2)))
l1=float(np.mean(np.abs(xp-x)+np.abs(yp-y)))

print("theta =",A)
print("M =",M)
print("X =",X)
print("RMSE =",rmse)
print("L1 =",l1)
