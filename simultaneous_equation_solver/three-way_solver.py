from fractions import Fraction

def solver(first, second, third):
    a1, b1, c1, d1 = first[0:4]
    a2, b2, c2, d2 = second[0:4]
    a3, b3, c3, d3 = third[0:4]

    delta = ((a1*b2*c3 + a3*b1*c2 + a2*b3*c1) - (a3*b2*c1 + a2*b1*c3 + a1*b3*c2))

    x = Fraction(((b2*c3*d1 + b1*c2*d3 + b3*c1*d2) - (b2*c1*d3 + b1*c3*d2 + b3*c2*d1)) ,delta)

    y = Fraction(((a1*c3*d2 + a3*c2*d1 + a2*c1*d3) - (a3*c1*d2 + a2*c3*d1 + a1*c2*d3)) ,delta)

    z = Fraction(((a1*b2*d3 + a3*b1*d2 + a2*b3*d1) - (a3*b2*d1 + a2*b1*d3 + a1*b3*d2)) ,delta)

    return [x, y, z]

#first_equation = "3x+2y+z=4"
#second_equation = "4x + 3y + 2z = 7"
#third_equation =  "2x - 2y + 3z = 5"
#test = third_equation.replace(" ","")
#print(test)
#test = list(map(int, test)) #리스트의 문자열을 int로 변환
#print(test)

temp = solver([3, 2, 1, 4], [4, 3, 2, 7], [2, 1, 3, 5])
print(temp)


