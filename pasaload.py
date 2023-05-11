import threading
import time
loadBalance = 1000
lock = threading.Lock()
def sendLoad(amount,phoneNumber):
    global loadBalance
    with lock:
        time.sleep(1)
        loadBalance-=amount
    print(f"{amount} is loaded to - {phoneNumber}")




loadAmount = [10,50,100]
loadchoice = []

print(f"Current load balance is {loadBalance}")

print("Choose load , ex: 1 2 3 or 1 2 , or 1")
print("""1-10 php
2-50 php
3-100 php
4 - exit
""")

while True:
    loadInput = input("\nEnter choices :")
    inputList = list(map(int,loadInput.split()))
    threadList = []
    if 4 in inputList:
        break
    for x in inputList:
        thread = threading.Thread(target=sendLoad,args=(loadAmount[x-1],"09983135775"))
        threadList.append(thread)

    for threads in threadList:
         threads.start()

    for threads in threadList:
        threads.join()   
    print(f"\ntotal amount balance {loadBalance}")

