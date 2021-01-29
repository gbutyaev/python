										#Правильная дата (7)
#Написать функцию date, принимающую 3 аргумента — день, месяц и год. Вернуть True, если такая дата есть в нашем календаре, и False иначе.




def date (day,month,year):
    if (day>=0 and day<=29) and month==2 and year%4==0 and (year%100!=0 or year%400==0):
        return("True")
    if day>0 and day<=30 and month==4 or month==6 or month==9 or month==11 and year>0:
        return("True")
    if day>0 and day<=31 and month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12 and year>0:
        return("True")
    if (day>=0 and day<=28) and month==2 and year>0:
        return("True")
    else:
        return("False")
    
    
date(28,2,2020)
