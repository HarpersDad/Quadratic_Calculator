import math
import numpy as np
import matplotlib.pyplot as plt


def goDoMath(varA, varB, varC):
    if vertY(varA, varB, varC) > 0:
        print("There are no X-intercepts for this function.")
    elif vertY(varA, varB, varC) == 0:
        print("The X intercept for this function is: ", vertX(varA, varB))
    else:
        quadCalc1(varA, varB, varC)

    print("This is your quadratic equation: y = (", varA, ")x^2 + (", varB, ")x + (", varC, ")", sep='')
    print("The vertex for the function is: (", vertX(varA, varB), ",", vertY(varA, varB, varC), ")")
    print("Y intercept: ", varC)

    plt.title("y = (" + varA + ")x^2 + (" + varB + ")X + (" + varC + ")")

    graphFunction(varA, varB, varC)

def graphFunction(a, b, c):
    x = np.linspace(-10, 10, 100)
    y = (int(a) * (x * x)) + (int(b) * x) + int(c)

    plt.plot(x, y)
    plt.show()


def quadCalc1(x, y, z):
    a = float(x)
    b = float(y)
    c = float(z)

    negB = -1*b
    B2 = math.pow(b,2)
    fourAC = (4*a*c)
    squirt = B2-fourAC
    over2A = 2*a

    if squirt <= 0:
        return print("There are no X-intercepts for this function.")
    else:
        top = float(negB + math.sqrt(squirt))
        answer = top / over2A
        return print("The X-intercepts for this function are: ", round(answer, 4), "and", quadCalc2(x, y, z))


def quadCalc2(x, y, z):
    a = float(x)
    b = float(y)
    c = float(z)

    negB = -1*b
    B2 = math.pow(b, 2)
    fourAC = (4*a*c)
    squirt = B2-fourAC
    over2A = 2*a

    top = negB - math.sqrt(squirt)
    answer = top / over2A

    return round(answer, 4)


def vertX(x, y):
    a = float(x)
    b = float(y)

    negB = -1*b
    over2A = 2*a
    answer = negB / over2A

    return round(answer, 4)


def vertY(x, y, z):
    a = float(x)
    b = float(y)
    c = float(z)

    negB = -1 * b
    over2A = 2 * a
    vertX = negB / over2A
    vertX2 = math.pow(vertX, 2)
    answer = (a*vertX2) + (b*vertX) + c

    return round(answer, 4)


def main():
    print("y = (a)x^2 + (b)x + (c)")

    varA = input("Enter a number for a: ")
    varB = input("Enter a number for b: ")
    varC = input("Enter a number for c: ")

    print("\nAll outputs have been rounded at most to the 4th decimal place.\n")

    if int (varA) == 0:
        print("You have given us a line, not a parabola.")

    else:
        goDoMath(varA, varB, varC)


main()
