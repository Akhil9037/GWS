# Equation 7 from the miller pdf  (try to solve completly for h_plus only)
# for the H plus polarization

from scipy.integrate import odeint
from math import*
from matplotlib.pyplot import*
from numpy import*
#from SciPy .integral import*

mu=1
D=arange(0,10,100)
theta=pi/4
t=arange(-0.5,1,100)
def ph(t):
    ph1=arange(0,60,10)
    return ph1
def r(t):
    r1=a*(1-e*e)/(1+e*cos(si))
    return r1
def r_dot(t):
    r2=odeint(r(t))
    return r2
def r_2dot(t):
    r3=odeint(r_dot(t))
    return r3

# for ph_dot
m_1=1
m_2=2
a=.5
r=0.5
G=6.67*10**(-11)
t=arange(-0.5,1,100)
L=(2*G*m_1*m_2*m_2)**(.5)*((1/(a*(1+e)))+(1/(a*(1-e))))**(-.5)

E=(((-G*m_1*m_2)/(2*a))/(mu))+1

def ph_dot(t):
    p=(L*(1+E)*r^(3))/(mu*sin(theta)*sin(theta)*(r-2))
    return p
def ph_2dot(t):
    p2=odient(ph_dot(t))
    return p2
   
h=0.0
    
def f(h):
    y=(mu/2*D)*((1-2*cos(2*theta)*cos(ph(t))))#*cos(ph(t))-3*cos(2*(ph(t)))*r_dot(t)*r_dot(t)+(3*cos(2*theta))*(2*cos(2*ph(t))*ph_dot(t)*ph_dot(t)+sin(2*ph(t))*ph_2dot(t))*r(t)*r(t)+(4*(3+cos(2*theta))*sin(2*ph(t))*ph_dot(t)*r_dot(t)+(1-2*cos(2*theta)*cos(ph(t))*cos(ph(t))-3*cos(2*ph(t)))*r_2dot(t))*r(t)))
    return y
h=1+f(h)

time=arange(-0.5,1,100)
plot(time,h)
show()
