
from sys import argv

script_name, output, rate, prize = argv

print("Выработка: ", output)
print("Ставка: ", rate)
print("Премия: ", prize)

price = int(output) * int(rate) + int(prize)
print("К выплате: ", price)
