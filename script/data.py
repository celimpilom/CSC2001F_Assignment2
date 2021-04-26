def numbers(file):
    with open(file, 'r') as f:
        names = []
        for line in f:
            line = line.strip()
            if line.isdigit():
                names.append(int(line))
        f.close()
    return names


for n in range(5, 26, 5):
    with open(f"files/cases/n{n}.txt", 'w') as case:
        names = numbers(f"files/data/AVL_{n}.txt")
        case.write(f"When n is(AVL) {n}\n")
        case.writelines(f"min: \n {min(names)}\n")
        case.writelines(f"max: \n {max(names)}\n")
        case.writelines(f"average: \n {sum(names)/len(names)}\n")
        
