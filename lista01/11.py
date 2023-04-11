import math

cat = int(input("cateto: "))
cat2 = int(input("cateto 2: "))

hip = (cat * cat) + (cat2 * cat2)
hip = math.sqrt(hip)

print("o valor da hipotenusa é: ", hip)