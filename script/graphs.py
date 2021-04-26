import numpy
import pandas
import matplotlib.pyplot


table = pandas.DataFrame(columns=["Best case", "Worst case", "Average case"], index = [n for n in range(500, 5001, 500)])

for n in range(500, 5001, 500):
    i = 0
    with open(f"./files/cases/find_n{n}.txt", 'r') as f:
        case = []
        for line in f:
            if line.strip().isdigit() or line.strip().replace(".","",1).isdigit():
                case.append(eval(line.strip()))
                
        print(case)
        table.loc[n] = case
    i += 1

table.plot()
matplotlib.pyplot.title("AVL find graphs cases")
matplotlib.pyplot.xlabel('n')
matplotlib.pyplot.ylabel("Count")
matplotlib.pyplot.savefig("./script/findgraph.png")
# table = pandas.DataFrame(columns=pandas.MultiIndex.from_arrays([['find' for i in range(3)]+['insert' for i in range(3)], ["Best case", "Worst case", "Average case"]*2]), index = [n for n in range(500, 5001, 500)])

# for n in range(500, 5001, 500):
#         i = 0
#         case = []
#         for method in ['find', 'insert']:
#             with open(f"./files/cases/{method}_n{n}.txt", 'r') as f:
#                 for line in f:
#                     if line.strip().isdigit() or line.strip().replace(".","",1).isdigit():
#                         case.append(eval(line.strip()))
#         table.loc[n] = case
#         i += 1

# table.plot()
# matplotlib.pyplot.title("AVL Find VS Insert")
# matplotlib.pyplot.xlabel('n')
# matplotlib.pyplot.ylabel("Count")
# matplotlib.pyplot.savefig("./script/graph.png")
