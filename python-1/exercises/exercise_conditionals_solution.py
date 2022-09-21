def greater_num(num1, num2):
  if num1 > num2:
    return num1
  else:
    return num2

def lesser_num(num1, num2):
  if num1 < num2:
    return num1
  else:
    return num2

def assign_grade(score):
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 65:
    return "D"
  else:
    return "F"

def hello_world(language_code):
  if language_code == "es":
    return "Hola, Mundo"
  elif language_code == "pt":
    return "Olá, Mundo"
  return "Hello, World"

def pluralize(noun, number):
  singular = str(number) + ' ' + noun
  if number == 1:
    return singular
  else:
    return singular + 's'