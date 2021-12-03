"""
1. Програма-світлофор.
    Створити програму-емулятор світлофора для авто і пішоходів.
    Після запуска програми на екран виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора.
    Кожну секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах.
    Приблизний результат роботи наступний:

      Red        Green

      Red        Green

      Red        Green

      Red        Green

      Yellow     Green

      Yellow     Green

      Green      Red

      Green      Red

      Green      Red

      Green      Red

      Yellow     Red

      Yellow     Red

      Red        Green

      .......
"""
import time


def traffic_light():
    red_green = ("Red", "Green")
    yellow_green = ("Yellow", "Green")
    yellow_red = ("Yellow", "Red")
    green_red = ("Green", "Red")

    while True:
        if red_green == ("Red", "Green") and yellow_green == ("Yellow", "Green") \
                and yellow_red == ("Yellow", "Red") and green_red == ("Green", "Red"):
            for i in range(4):
                print(f"{red_green[0]:10}{red_green[1]}")
                time.sleep(1)
            for i in range(2):
                print(f"{yellow_green[0]:10}{yellow_green[1]}")
                time.sleep(1)
            for i in range(4):
                print(f"{green_red[0]:10}{green_red[1]}")
                time.sleep(1)
            for i in range(2):
                print(f"{yellow_red[0]:10}{yellow_red[1]}")
                time.sleep(1)
        else:
            print(f"{yellow_red[0]:10}{yellow_red[1]}")
            time.sleep(1)


print(traffic_light())
