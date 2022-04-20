from generadores import glc, media_cuadrados, generadorNumpy



generator = glc(3146, 12, 15, 87, 20)

numbers = generator.generate()

print(numbers)
