import random

main = []

def addnewrandom (array): #добавление случайной особи
    newlist = [0,1,2,3,4,5,6,7]
    random.shuffle(newlist)
    if newlist not in array:  #проверка на наличие похожих в array
        #print('не совпало')
        array.append(newlist)
    else:
        print ('совпало')
    
def mutationwithadd (numb, array):#мутация с добавлением в список
    ran1 = random.randint(0,7)
    ran2 = random.randint(0,7)
    if ran1==ran2:
        #print("равны")
        ran1-=1
    print(ran1)
    print(ran2)
    newnumb = list(array[numb])
    newnumb[ran1],newnumb[ran2]=newnumb[ran2],newnumb[ran1] #меняем местами
    if newnumb not in (array):#проверка на наличие такого же
        array.append(newnumb)#добавляем в список
        #print('не совпало')
     #else:
        #print('совпало')

def mutation (numb,array): #мутация без добавления в список (унарная операция)
    ran1 = random.randint(0,7)
    ran2 = random.randint(0,7)
    if ran1==ran2:
        #print("равны")
        ran1-=1
    array[numb][ran1],array[numb][ran2]=array[numb][ran2],array[numb][ran1]
			
def crossingover (num1,num2,array): #бинарная операция
	index1 = random.randint(0,7) #создание числа от 0 до 7 это индекс 1 родителя 1 числа перестановки
	#print("придуманный индекс ",index1)
	saved1 = array[num1][index1] #сохранение полученного числа в 1 родителе под случайным индексом
	saved2 = array[num2][index1] #сохранение полученного числа в 2 родителе под случайным индексом
	array[num1][index1],array[num1][array[num1].index(saved2)]=array[num1][array[num1].index(saved2)],array[num1][index1]#меняем местами
	array[num2][index1],array[num2][array[num2].index(saved1)]=array[num2][array[num2].index(saved1)],array[num2][index1]#меняем местами
	
def Fitness (num,array):#вычисление Фитнесс-функции
    F=0
    lis = list(array[num])
    unic = []
    counterunic = []
    for i in lis:
        clockwise = i - lis.index(i)
        unic.append(clockwise)
        counterclockwise = -i - lis.index(i)
        counterunic.append(counterclockwise)
    setun = set(unic)
    setcon = set(counterunic)
    F=F+len(unic)-len(setun)
    F=F+len(counterunic)-len(setcon)
    Fit=1/(1+F)
    return Fit
        
def Weights(array,from1=0):#создание списка весов на основе фитнесс-функции
    Fitarray=[]            #сам не знаю зачем написал эту функцию
    i=0
    while i < len(array):
        Fitarray.append(Fitness(i,array))
        i+=1
    return Fitarray
    #print(Fitarray)
    
def ruller(weight):#рулетка
    roll = random.random()
    if roll<weight:
        return True
    if roll>weight:
        return False





