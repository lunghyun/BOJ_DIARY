n = input()
if n != "#":
    while(n != "#"):
        temp = 0
        temp += n.count("a")
        temp += n.count("A")
        temp += n.count("e")
        temp += n.count("E")
        temp += n.count("i")
        temp += n.count("I")
        temp += n.count("o")
        temp += n.count("O")
        temp += n.count("u")
        temp += n.count("U")
        print(temp)
        n = input()