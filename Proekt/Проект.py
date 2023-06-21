import random


def askForGuess():
 while True:

  guess = input('> ') # Введите свое предположение.

  if guess.isdecimal():
   return int(guess) # Преобразуем строковое представление
                     # предположения в число.
  print('Введите число от 1 до 200.')

print('Угадай число')
print()
secretNumber = random.randint(1, 200) # Выбираем случайное число.
print('Я думаю о числе от 1 до 200.')

for i in range(15): # У игрока есть 15 попыток.
 print('У вас осталось {} догадок. Предположить.'.format(15 - i))

 guess = askForGuess()
 if guess == secretNumber:
  break # Если число угадано — выходим из цикла.

# Даем подсказку:
 if guess < secretNumber:
  print('Ваша догадка слишком низкая.')
 if guess > secretNumber:
  print('Ваша догадка слишком высокая.')

# Раскрываем результаты:
if guess == secretNumber:
 print('Ура! Ты угадал мой номер!')
else:
 print('Игра закончена. Число, о котором я думал, было', secretNumber)




