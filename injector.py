import psutil
from pyinjector import inject 
import time



def checkIfProcessRunning(processName):


    for proc in psutil.process_iter():
        try:
        
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;
def findProcessIdByName(processName):

    listOfProcessObjects = []
    #Iterate over the all the running process
    for proc in psutil.process_iter():
       try:
           pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
         
           if processName.lower() in pinfo['name'].lower() :
               listOfProcessObjects.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
           pass

    return listOfProcessObjects;

def injectClient():
    if checkIfProcessRunning('javaw'):
        print('Minecraft was found')
        listOfProcessIds = findProcessIdByName('javaw')
        if len(listOfProcessIds) > 0:
            for elem in listOfProcessIds:
                processID = elem['pid']
                processName = elem['name']
                processCreationTime =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(elem['create_time']))
                print((processID ,processName,processCreationTime ))
            inject (processID, "eternal_internal.dll")
            print("Injection was sucsessful. Injector now will close")
            
    else:
        print('Minecraft was not found. Please run minecraft and try again.')

injectClient()
time.sleep(1)

