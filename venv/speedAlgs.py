import math

def callAlg(alg, input):
    if alg == "1":
        return alg1(input)
    if alg == "2":
        return alg2(input)
    if alg == "3":
        return alg3(input)
    if alg == "4":
        return alg4(input)
    if alg == "5":
        return alg5(input)
    if alg == "6":
        return alg6(input)
    if alg == "7":
        return alg7(input)
    if alg == "8":
        return alg8(input)
    elif alg == "counterclockwise":
        return input
    else:
        return -input

def clockwise(input):
    return -input

def counterclockwise(input):
    return input

# fast - slows down - reverses
# (-(.3x-7)^2)+49
def alg1(input):
    if input > 46.667:
        input -= 46.667
    return (-(.3*input-7)**2)+49

# speeds up super fast - slowly increases
# sqrt(20x)
def alg2(input):
    return math.sqrt(90*input)

# starts slow - blasts off
# .001x^3
def alg3(input):
    return ((.1*input+1)**3)

# goes backwards - slows down - reverses to go forward
# (.25x-5\right)^2
def alg4(input):
    return ((.25*input-5)**2)

# goes backwards fast - slows down but keeps going backwards
# -sqrt(30x)+40
def alg5(input):
    return (-(math.sqrt(30*input))+40)

# sine wave, forward - reverses - reverses...etc
# 5sinx+5
def alg6(input):
    return 20*math.sin(0.5*input)+5

# jerks to left over and over
# slow - super fast - slow - super fast....etc
# 3tan.15x+20
def alg7(input):
    return 2*math.tan(0.2*input)+5

# slower sine wave (alg6)
# 20sin.1x+5
def alg8(input):
    return 20*math.sin(.1*input)