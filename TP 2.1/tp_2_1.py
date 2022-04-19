from generadores import glc, media_cuadrados, generadorNumpy



generator = glc(6545, 12, 87, 63, 100)

numbers = generator.generate()

print(numbers)
