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

def changeNumber():
    phoneNumber = input("Enter Phone Number: ")
    print(f"Password Changed to {phoneNumber}")
    return phoneNumber
def showMenu():
    print(f"Current load balance is {loadBalance}")
    print("Choose load , ex: 1 2 3 or 1 2 , or 1")
    print("""1-10 php
2-50 php
3-100 php
4 - exit
5 - Change Number
""")


phoneNumber = changeNumber()
loadAmount = [10,50,100]
loadchoice = []

while True:
    showMenu()
    loadInput = input("\nEnter choices :")
    if loadInput == "5":
      phoneNumber =  changeNumber()
      continue
    inputList = list(map(int,loadInput.split()))
    threadList = []
    if 4 in inputList:
        break
    for x in inputList:
        thread = threading.Thread(target=sendLoad,args=(loadAmount[x-1],phoneNumber))
        threadList.append(thread)
    
    for threads in threadList:
         threads.start()

    for threads in threadList:
        threads.join()   

