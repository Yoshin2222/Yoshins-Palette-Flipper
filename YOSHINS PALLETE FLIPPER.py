
def main():
    import os
    flip = "_Flipped"
    act = ".act"
    print("YOSHINS PALMOD/TM PAL FLIPPER")
    pal_length = 0x30

    while 1:
        print("ENTER THE NAME OF THE PALLETE YOU'D LIKE TO FLIP")
        name = input("NAME = ")
        actname = name + act
        while not os.path.exists(actname):
            print("INVALID FILENAME! INPUT SOMETHING ELSE")
            name = input("NAME = ")
            actname = name + act

        flipname = name+flip+act
        print("Now flipping file {}...".format(flipname))
        #Begin flipping
        with open(actname, "rb") as inp:
            temp,temp2 = inp.read(),[] #Make a copy of the file we can mess with]
        size = len(temp)
        for x in range(0,size,pal_length):
            #Append the rest of the data to the end
            if x + pal_length >= size:
                for i in range(len(temp2),size,1):
                    temp2.append(temp[i])
                break
            #Append the rest of the palette data
            for i in range(3,pal_length,1):
                temp2.append(temp[x+i])
            #Append the first colour first
            for i in range(0,3,1):
                temp2.append(temp[x+i])

        with open(flipname, "wb") as out:
            out.write(bytes(temp2))


if __name__ == "__main__":
    main()

