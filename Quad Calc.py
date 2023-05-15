import math
import numpy as np
import matplotlib.pyplot as plt

def graphFunction(a, b, c):
    x = np.linspace(-10, 10, 100)
    y = (int(a) * (x * x)) + (int(b) * x) + int(c)

    plt.plot(x, y)
    plt.show()

def quadCalc1(x, y, z):
    a = float(x);
    b = float(y);
    c = float(z);

    negB = -1*b;
    B2 = math.pow(b,2);
    fourAC = (4*a*c);
    over2A = 2*a;

    top = negB + math.sqrt(B2 - fourAC);

    answer = top / over2A;

    return answer;

def quadCalc2(x, y, z):
    a = float(x);
    b = float(y);
    c = float(z);

    negB = -1 * b;
    B2 = math.pow(b, 2);
    fourAC = (4 * a * c);
    over2A = 2 * a;

    top = negB - math.sqrt(B2 - fourAC);

    answer = top / over2A;

    return answer;


def vertX(x, y):
    a = float(x);
    b = float(y);

    negB = -1*b;
    over2A = 2*a;

    answer = negB / over2A;
    return answer;


def vertY(x, y, z):
    a = float(x);
    b = float(y);
    c = float(z);

    negB = -1 * b;
    over2A = 2 * a;

    vertX = negB / over2A;
    vertX2 = math.pow(vertX, 2);

    answer = (a*vertX2) + (b*vertX) + c;
    
    return answer;


def main():
    print("y = (a)x^2 + (b)x + (c)");

    varA = input("Enter a number for a: ");
    varB = input("Enter a number for b: ");
    varC = input("Enter a number for c: ");

    print("This is your quadratic equation: y = (",varA,")x^2 + (",varB,")x + (",varC,")", sep='');

    if vertY(varA, varB, varC) > 0:
        print("There are no X intercepts for this function.");
    elif vertY(varA, varB, varC) == 0:
        print("The X intercept for this function is: ", vertX(varA, varB));
    else:
        print("The X intercepts for this function are: ", quadCalc1(varA, varB, varC), "and", quadCalc2(varA, varB, varC));

    print("The vertex for the function is: (", vertX(varA, varB), ",", vertY(varA, varB, varC), ")");
    print("Y intercept: ", varC);

    graphFunction(varA, varB, varC)

main()
