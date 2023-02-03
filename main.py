# GLOBAL VARIABLES
items_arr = []

def ins_calc(insurance):
    # goes to insurance
    if insurance == 1:
        print("The insurance is insurance1")
        return ins1()

    elif insurance == 2:
        print("The insurance is insurance2")
        return ins2()
    
    elif insurance == 3:
        print("The insurance is insurance3")
        return ins3()

def ins1():
    ins1_items = [
        ["A7030", 96.09],
        ["A7031", 36.54],
        ["A7032", 20.43],
        ["A7033", 20.43],
        ["A7034",60.12],
        ["A7035", 19.88],
        ["A7037", 12.85],
        ["A7038", 13.46],
        ["A7039", 6.54],
        ["A7046", 13.99]
        ]
    ins1_price = []
    ins1_sum = 0

    # gets item code until finished
    item = ""
    while item != "done":
        item = input("Enter item code: ")
        items_arr.append(item)
        
        for i in range(len(ins1_items)):
            if item == ins1_items[i][0]:
                ins1_price.append(ins1_items[i][1])
                ins1_sum += ins1_items[i][1]
                print("########## TOTAL: " + str(ins1_sum))
        print(items_arr)
        

    return ("########## TOTAL: " + str(ins1_sum))

def ins2():
    ins2_items = [
        ["A7030", 100.66],
        ["A7031", 57.40],
        ["A7032", 25.00],
        ["A7033", 25.00],
        ["A7034", 54.90],
        ["A7035", 25.62],
        ["A7037", 16.64],
        ["A7038", 54.90],
        ["A7039", 13.56],
        ["A7046", 9.18]
        ]
    ins2_price = []
    ins2_sum = 0

    # gets item code until finished
    item = ""
    while item != "done":
        item = input("Enter item code: ")
        items_arr.append(item)
        
        for i in range(len(ins2_items)):
            if item == ins2_items[i][0]:
                ins2_price.append(ins2_items[i][1])
                ins2_sum += ins2_items[i][1]
                print("########## TOTAL: " + str(ins2_sum))
        print(items_arr)
        

    return ("########## TOTAL: " + str(ins2_sum))

def ins3():
    ins3_items = [
        ["A7030", 72.56],
        ["A7031", 26.84],
        ["A7032", 25.00],
        ["A7033", 25.00],
        ["A7034", 50.00],
        ["A7035", 15.29],
        ["A7037", 15.78],
        ["A7038", 12.48],
        ["A7039", 11.64],
        ["A7046", 7.51]
        ]
    ins3_price = []
    ins3_sum = 0

    # gets item code until finished
    item = ""
    while item != "done":
        item = input("Enter item code: ")
        items_arr.append(item)
        
        for i in range(len(ins3_items)):
            if item == ins3_items[i][0]:
                ins3_price.append(ins3_items[i][1])
                ins3_sum += ins3_items[i][1]
                print("########## TOTAL: " + str(ins3_sum))
        print(items_arr)
        

    return ("########## TOTAL: " + str(ins3_sum))




if __name__ == "__main__":
    print("---DEDUCTIBLE CALCULATOR---")
    print("What is the insurance?\n1. Insurance 1\n2. Insurance 2\n3. Insurance 3\n")
    insurance = int(input("Enter a number: "))
    print(ins_calc(insurance))
