import random
import os
import numpy
import pandas
import matplotlib.pyplot

def openList(file):
    with open(file, 'r') as f:
        names = []
        for line in f:
            #id = line.split(" ")[0]
            names.append(line)
        f.close()
    return names

def tester(names, start, stop, step):
    for n in range(start, stop + 1, step):
        list = random.sample(names, n)
        with open(f"files/inputs/AVL_{n}.txt", 'w') as f:
            for line in list:
                f.writelines(line)
            f.close()
        for student in list:
            id = student.split(" ")[0]
            os.system(f"make run stdN={id} file=inputs/AVL_{n}.txt >> files/data/AVL_{n}.txt")

def numbers(file):
    with open(file, 'r') as f:
        names = []
        for line in f:
            line = line.strip()
            if line.isdigit():
                names.append(int(line))
        f.close()

    insert = [i for i in names if i%2 == 0]
    count = [i for i in names if i%2 != 0]
    return insert, count

if __name__ == "__main__":
    print("---------------------------------------------")
    print("                 TEST APP")
    print("---------------------------------------------")
    print()
    inputs = input("Enter Interval <start> <stop> <step>:\n")
    inputs_list = inputs.split(" ")
    start = eval(inputs_list[0])
    stop = eval(inputs_list[1])
    step = eval(inputs_list[2])

    names = openList('files/oklist.txt')
    tester(names, start, stop, step)

    #----------------------------------------------------------------
    # DATA
    for n in range(start, stop + 1, step):
        for i, method in enumerate(['insert', 'find']):
            with open(f"files/cases/{method}_n{n}.txt", 'w') as case:
                result = numbers(f"files/data/AVL_{n}.txt")
                case.write(f"{method} count When n is {n}\n")
                case.writelines(f"min: \n {min(result[i])}\n")
                case.writelines(f"max: \n {max(result[i])}\n")
                case.writelines(f"average: \n {sum(result[i])/len(result[i])}\n")
    
    #---------------------------------------------------------------------
    # GRAPH
    table = pandas.DataFrame(columns=pandas.MultiIndex.from_arrays([['find' for i in range(3)]+['insert' for i in range(3)], ["Best case", "Worst case", "Average case"]*2]), index = [n for n in range(500, 5001, 500)])

    for n in range(start, stop + 1, step):
        i = 0
        case = []
        for method in ['find', 'insert']:
            with open(f"./files/cases/{method}_n{n}.txt", 'r') as f:
                for line in f:
                    if line.strip().isdigit() or line.strip().replace(".","",1).isdigit():
                        case.append(eval(line.strip()))
        table.loc[n] = case
        i += 1

    table.plot()
    matplotlib.pyplot.title("AVL Find VS Insert")
    matplotlib.pyplot.xlabel('n')
    matplotlib.pyplot.ylabel("Count")
    matplotlib.pyplot.savefig("./script/graph.png")

    print("DONE - Check for graphs on the script folder")
    print("---------------------------------------------")