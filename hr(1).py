# -*- coding: utf-8 -*-
"""HR(1).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WN2fbXmxJmHxtsQdNNvfCxQS1LjSHLWb
"""

import numpy as np

data = np.array([100,80,240,230,180,160,150,210,250,230,260,215,270,175,145,190,320,300,390,235,160,195,180,215,220,210,60,120,130,250])

mean = np.mean(data)

disp = np.var(data,ddof=1)

std = np.std(data,ddof=1)

mean,disp,std

"""#### Single Hindmarsh-Rose neuron

\begin{equation}
\begin{array}{l}
\dot{x} = y - ax^3+bx^2+I-z\\
\dot{y} = c-dx^2-y\\
\dot{z} = r(s(x - x_{rest}) - z)
\end{array}
\end{equation}
"""

import numpy as np
import scipy as scp
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import sympy as sp
sp.init_printing()

a = 0.1



def HR2(a):
  def rhs(t,X):
    r, f = X
    return [2*r-a*r*f,-f+a*r*f]
  return rhs

def main(a,r0,f0):
  rhs = HR2(a)
  sol = solve_ivp(rhs, [0, 10], [r0, f0], rtol = 1e-11, atol = 1e-11, dense_output=True)
  ts = sol.t
  xs, ys = sol.y
  plt.figure(figsize=(9, 3),constrained_layout=True)

  plt.subplot(131)
  plt.plot(xs,ys)
  plt.xlabel('r')
  plt.ylabel('f')
  plt.subplot(132)
  plt.plot(xs)
  plt.xlabel('t')
  plt.ylabel('r')
  plt.subplot(133)
  plt.plot(ys)
  plt.xlabel('f')
  plt.ylabel('t')
  plt.suptitle('Графики')
  plt.show()
  # print(xs,ys)

  return xs,ys

x1,y1 = main(0.1,100,10)
x4,y4 = main(0.1,10,10)
x2,y2 = main(0.1,0,200)
x3,y3 = main(0.1,0.000001,0)
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.plot(x4,y4)

ts = sol.t
xs, ys = sol.y

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.plot(xs,ys)
plt.xlabel('r')
plt.ylabel('f')
plt.subplot(132)
plt.plot(xs)
plt.xlabel('t')
plt.ylabel('r')
plt.subplot(133)
plt.plot(ys)
plt.xlabel('f')
plt.ylabel('t')
plt.suptitle('Графики')
plt.show()

fig = plt.figure()

plt.plot(ts, xs)
plt.xlabel(r'$t$')
plt.ylabel(r'$x$')

b = 3.5
r = 0.01
s = 4
I = 4.55

x_rest = -1.6
c = 1
a = 0.1
d = 5

def HR3(t, X):
    x, y, z = X
    return [y - a*x**3 + b*x**2 + I - z, c - d*x**2 - y, r*(s*(x - x_rest) - z)]
sol = solve_ivp(HR3, [0, 1000], [1, 1, 1], rtol = 1e-11, atol = 1e-11, dense_output=True)
ts = sol.t
xs, ys, zs = sol.y

len(xs)

ts1 = ts[74000:]
xs1 = xs[74000:]
ys1 = ys[74000:]
zs1 = zs[74000:]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(projection='3d')
ax.plot(xs1, ys1, zs1)
ax.scatter(xs1[0], ys1[0], zs1[0], c='g', label='Начало')
ax.scatter(xs1[-1], ys1[-1], zs1[-1], c='r', label='Конец')
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_zlabel("$z$")

fig = plt.figure()

plt.plot(ts1, xs1)
plt.xlabel(r'$t$')
plt.ylabel(r'$x$')

x_rest = -1.5
b = 2.5
r = 0.01
s = 4
I = 2.55

def HR3(t, X):
    x, y, z = X
    return [y - a*x**3 + b*x**2 + I - z, c - d*x**2 - y, r*(s*(x - x_rest) - z)]
sol = solve_ivp(HR3, [0, 1000], [0, 0, 0], rtol = 1e-11, atol = 1e-11, dense_output=True)
ts = sol.t
xs, ys, zs = sol.y

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(projection='3d')
ax.plot(xs, ys, zs)
ax.scatter(xs[0], ys[0], zs[0], c='g', label='Начало')
ax.scatter(xs[-1], ys[-1], zs[-1], c='r', label='Конец')
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_zlabel("$z$")

fig = plt.figure()

plt.plot(ts, xs)
plt.xlabel(r'$t$')
plt.ylabel(r'$x$')

b = 3.5
r = 0.01
s = 4
I = 2.55

def HR3(t, X):
    x, y, z = X
    return [y - a*x**3 + b*x**2 + I - z, c - d*x**2 - y, r*(s*(x - x_rest) - z)]
sol = solve_ivp(HR3, [0, 500], [0, 0, 0], rtol = 1e-11, atol = 1e-11, dense_output=True)
ts = sol.t
xs, ys, zs = sol.y

sol1 = solve_ivp(HR3, [0, 100], [10, 10, 10], rtol = 1e-11, atol = 1e-11, dense_output=True)
ts1 = sol1.t
xs1, ys1, zs1 = sol1.y

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(projection='3d')
ax.plot(xs, ys, zs)
ax.plot(xs1, ys1, zs1)
ax.scatter(xs[0], ys[0], zs[0], c='g', label='Начало')
ax.scatter(xs[-1], ys[-1], zs[-1], c='r', label='Конец')
ax.scatter(xs1[0], ys1[0], zs1[0], c='g', label='Начало')
ax.scatter(xs1[-1], ys1[-1], zs1[-1], c='r', label='Конец')
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_zlabel("$z$")

fig = plt.figure()

plt.plot(ts, xs)
plt.xlabel(r'$t$')
plt.ylabel(r'$x$')

fig = plt.figure()

plt.plot(ts1, xs1, c = 'orange')
plt.xlabel(r'$t$')
plt.ylabel(r'$x$')

def Plot_HR(a,c,d,x_rest,b,r,s,I):
    def HR3(t, X):
        x, y, z = X
        # return [y - a*x**3 + b*x**2 + I - z, c - d*x**2 - y, r*(s*(x - x_rest) - z)]
        return [y - a*x**3 + b*x**2 + I - z, c - d*x**2 - y, 0]

    fig = plt.figure()
    for i in range(-2, 3, 1):
      for j in range(-40, 3, 3):
        print([i,j])
        sol = solve_ivp(HR3, [0, 200], [i, j, 0], rtol = 1e-11, atol = 1e-11, dense_output=True)

        ts = sol.t
        xs, ys, zs = sol.y

        # fig = plt.figure(figsize=(10,10))
        # ax = fig.add_subplot(projection='3d')
        # ax.plot(xs, ys, zs)
        # ax.scatter(xs[0], ys[0], zs[0], c='g', label='Начало')
        # ax.scatter(xs[-1], ys[-1], zs[-1], c='r', label='Конец')
        # ax.set_xlabel("$x$")
        # ax.set_ylabel("$y$")
        # ax.set_zlabel("$z$")


        plt.plot(xs, ys, color='black')
        # plt.plot(ts, ys)
        plt.xlabel(r'$x$')
        plt.ylabel(r'$y$')

Plot_HR(1, 1, 5, -1.5, 3, 0.003, 2, 0.)

"""#### Map of regimes depending on governing parameters b and I"""

# import numpy as np
# import scipy as scp
# import matplotlib.pyplot as plt
# from scipy.integrate import solve_ivp

# a = 1
# c = 1
# d = 5
# x_rest = -1.6
# # b = 3.214
# r = 0.0021
# s = 4
# # I = 3.823
# def HR3(t, X, b, I):
#     x, y, z = X
#     return [y - a*x**3 + b*x**2 + I - z, c - d*x**2 - y, r*(s*(x - x_rest) - z)]

# surface = lambda x, y, z, b, I: y - x**3 + b*x**2 + I - z

# def evt(t, X, b, I):
#     x, y, z = X
#     return surface(x, y, z, b, I)

# evt.terminal = False
# evt.direction = 1

# def crossing(b, I):
#     crosscounter = 0
#     t_start = 0
#     t_finish = 500
#     x_start = 0
#     y_start = -4
#     z_start = 4

#     sol = solve_ivp(HR3, [t_start, t_finish], [x_start, y_start, z_start], rtol = 1e-11, atol = 1e-11,  events = evt, dense_output=True, args = (b, I))
#     ts = sol.t
#     xs, ys, zs = sol.y

#     dots = sol.y_events

#     pos_evts = [sol.sol(t) for t in sol.t_events]
#     ps_x, ps_y, ps_z = zip(*pos_evts)
#     ps_x = ps_x[0]
#     ps_y = ps_y[0]
#     ps_z = ps_z[0]

#     counter = 0

#     for i in range(len(ps_z)-1):
#         for j in range(len(ps_z) - 1):
#             if ps_z[i] == ps_z[j]:
#                 counter = counter + 1

#     crosscounter = counter
#     return crosscounter

# bs = np.linspace(0.5, 4.5, 5)
# Is = np.linspace(0.0, 5.5, 5)
# grid = np.zeros([len(Is), len(bs)])
# #print('bs =', len(bs))
# #print('Is =', len(Is))
# for i, I in enumerate(Is):
#     for j, b in enumerate(bs):
#         grid[i][j] = crossing(b, I)
#         #print('b = ', b, ' I = ', I, ' grid = ', grid[i][j])
# plt.pcolormesh(bs, Is, grid, cmap=plt.cm.get_cmap('jet'))
# plt.axes().set_aspect('equal', adjustable='box')
# plt.colorbar()