# T.C = O(n + 1) = O(n)
# S.C = O(n + 1) = O(n)

count = 0
def fun():
    global count
    if(count == 4):
        return
    count += 1
    fun()
    print("Arihant")

fun()

    