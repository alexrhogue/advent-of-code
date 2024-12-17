
def load_input(input_file: str):
    f = open(input_file, "r")
    lines = f.readlines()
    
    one = []
    two = []
    
    for line in lines:
        ids = line.split()
        one.append(int(ids[0]))
        two.append(int(ids[1]))
        
    one.sort()
    two.sort()
    
    return (one, two)


def calc_dist(one: list, two: list):
    dist = 0
    
    for i in range(len(one)):
        dist +=  abs(one[i] - two[i])
        
    return dist
        
        
def calc_similarity(one: list, two: list):
    two_count = {}
    for i in range(len(two)):
        id = two[i]
        two_count[id] = 1 + two_count.get(id, 0)
      
        
    similarity = 0
    for i in range(len(one)):
        id = one[i]
        similarity += id * two_count.get(id, 0)
      
    return similarity

def main():
    [one, two] = load_input("input.txt")
    
    dist = calc_dist(one, two)
    similarity = calc_similarity(one, two)
    
    print("dist", dist)
    print("similarity", similarity)
    
    
if __name__=="__main__":
    main()
