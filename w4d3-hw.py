#6kyu
#          O(n)
def order(sentence):
    new_list = []
    sentence = sentence.split()
    for i in range(1, len(sentence) + 1): #O(1)
        for j in sentence:
            if str(i) in j:
                new_list.append(j)
    return " ".join(new_list)


#7kyu
#                 O(n)
def is_triangular(t):
    level =1 #O(n)
    while t > 0:
        t -= level
        level += 1
    return t == 0



#7kyu

def get_sum(a,b):
    if a == b:
        return a
    small, big = sorted([a, b])
    
    return sum ([i for i in range (small, big +1)])