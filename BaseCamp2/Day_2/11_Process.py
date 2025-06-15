import multiprocessing
import threading
import time
from datetime import datetime

# Define a Task that is heavy in CPU time
def cpu_task (name : str, counter : int):

    # Execute a computation in loop to simulate
    Res = 0
    for i in range (counter):

        Res = Res + (((i ** 2) + 2.0) * 1.45)

    print ("Task "+name+" Executed. Result : ",str(Res))

# Execute with multi process
if __name__ == "__main__":
    # Execute with multi thread

    # Creating threads
    T1 = threading.Thread (target=cpu_task, args=("T1", 50000000))
    T2 = threading.Thread (target=cpu_task, args=("T2", 40000000))

    # take time stamp
    Before = datetime.now ()

    # Tasks as Thread
    T1.start ()
    T2.start ()

    # Wait for both to complete
    T1.join ()
    T2.join ()

    After = datetime.now ()

    print (After-Before)

    # Creating Process
    P1 = multiprocessing.Process (target=cpu_task, args=("P1", 50000000))
    P2 = multiprocessing.Process (target=cpu_task, args=("P2", 40000000))

    # take time stamp
    Before = datetime.now ()

    # Tasks as Thread
    P1.start ()
    P2.start ()

    # Wait for both to complete
    P1.join ()
    P2.join ()

    After = datetime.now ()

    print (After-Before)