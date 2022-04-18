from generadores import glc



generator = glc(6545, 12, 87, 63, 100)

numbers = generator.generate()

print(numbers)
