# letters = ["a","d", "z", "e", "h", "j"]
# numbers = [4,8,33,2,1,6]
# cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
# cars.sort(key=lambda e:len(e))
# print(cars)


def bubblesort(myList:list):
    while True:
        sorted = True
        for i in range(len(myList)-1):
            if myList[i] > myList[i+1]:
                sorted = False
                myList[i], myList[i+1] = myList[i+1], myList[i]
        if sorted:
            break
    print(myList)
bubblesort([6,5,3,1,8,7,2,4])