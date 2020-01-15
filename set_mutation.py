def mutate_string(string, position, character):
    listA=list(string)
    print(listA)
    listA[position]=character
    print(listA)
    return ''.join(listA)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)