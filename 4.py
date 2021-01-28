

										#Времена года (4)
#Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).



def seasons(x):
    if x < 4:
        return("winter")
    if x >=4 and x < 7 :
        return("spring")
    if x >6 and x < 10:
        return("summer")
    if x >9 and x <13:
        return("autumn")
seasons(7)Времена года (4)

