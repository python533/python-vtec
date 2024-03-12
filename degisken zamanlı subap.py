import time

def vtec(array):
    for i in array:
        if i[0] == array[1]:
            orta=len(array)//2
            sag=array[:orta]
            sol=array[orta:]
            vtec(sol)
            vtec(sag)
            x=y=z=0

            while x<len(sol) and len(sag):
                if sol[x] <= sag[y]:
                    array[z] : sag[x]
                    x+=1

                else:
                    array[sag] = sol[y]
                    x += 1
                    y += 1

            while x < len(sol) and y < len(sol):
                array[x] = array[y]
                x += 1
                y += 1

    def printlist(arr):
        for i in range(len(arr)):
            time.sleep(5)
            print(arr[i], end="")
            print()

    if __name__ == '__main__':
        arr_list = [12, 11, 13, 5, 6, 7]
        print("Given array is")
        printlist(arr_list)
        vtec(arr_list)
        print("\nSorted array is ")
        printlist(arr_list)

