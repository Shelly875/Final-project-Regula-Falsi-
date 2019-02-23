![alt text](https://i.ytimg.com/vi/pg1I8AG59Ik/maxresdefault.jpg)
#    Numerical analysis final project - Regula falsi


# Author 
Shelly Miron

# Introduction 

In this project I will discuss the functionality of the "Regula-Falsi method" as a numerical method 
for finding a high-level polynomial root as part of the final project in Numerical analysis course.

The guiding principle of the Regula Falsi method is like the secant method, the use of a succession 
of zeros of secant lines obtained from two-point interpolation to better approximate a zero of a function f (x).
f (x) represents the function whose zero we are trying to find.
A key difference between the Regula Falsi method and the secant method is that in
the first step of the Regula Falsi method, the two initial estimates, x0 and x1, are chosen
such that f (x0) and f (x1) are of opposite signs ( f (x0) f (x1) < 0). This is unlike the
secant method, where there is no restriction that the initial estimates bracket a zero.

The iteration is the Regula Falsi method, where x is an endpoint of the original bracketing interval
that remains fixed. At each step of the Regula Falsi method, the current approximation replaces the previous interval endpoint whose corresponding function value has the same sign as the current best estimate of x, while the other interval endpoint is
retained.

--- 

# Documentation

```
The params the 'regula falsi' program recived:

 :param f: a polynomial (sent as lambda or function)
 :param x0: the first x point of an interval
 :param x1: the second x point of an interval
 :param acceptable_error: the max error for stopping the calculation
 :return: the root of a given polynomial
 
 Input : regula_falsi(f, x0, x1, acceptable_error)
 Output: the root of the polynomial (f) in particular range
 
```

# How to use

![GIF](http://g.recordit.co/a6u2fcW6UI.gif)


# Installation

1. Download to your PC the last update version of python (I used Python 3.7) : https://www.python.org/
2. Download PyCharm from JetBrain: https://www.jetbrains.com/pycharm/
3. Open my code in Pycharm and run it as shown in the gif above
4. Run test.py to check code reliability

# History and scientific sources

* https://ece.uwaterloo.ca/~dwharder/NumericalAnalysis/10RootFinding/falseposition/
* https://books.google.co.il/books?id=jfQ9E0u4pLAC&pg=PA147&redir_esc=y#v=onepage&q=regula&f=false
* http://mathworld.wolfram.com/MethodofFalsePosition.html

---

# Test Cases

![GIF](http://g.recordit.co/PGW21CWXft.gif)

* Using 'unittest' package


# Version

Currently my final version of the software.

# License

This project is licensed under the GNU GENERAL PUBLIC LICENSE since 2007 above : [GNU GENERAL PUBLIC LICENSE](https://github.com/Shelly875/Final-project-regula-falsi/blob/master/LICENSE) © .





