# '''
# Race Condition
# 2.synchronixation 
# 3.lock 
# 4.Rlock

# '''
# # why we need sycronization
# '''
# balance = 1000
# thread -1 ---withdraw 500
# thread -2 ---withdraw 700

# both are accessing the same variable
# without proper control


# Incorrect balance
# wrong transaction
# data corrupts
# to avoid the above we will use:
# Synchronization :
# this is a process of controlling access to shared
# resources so that only one thread modifies at a time 

# Lock :
# hared 
# resources : any variable,file,database,object

# Example :
# count = 0
# if multiple threads modifies count simultaneously
 
# #Race Condition :
# occurs when multiple threads access and modify
# shared data simultaneously causing unpredictable
# outputs :

# '''
# # count = 0
# # count+=1
# # print(count)

# #write with threads 
# # import threading
# # count = 0
# # def incerement():
# #     global count
# #     count+=1
# # threads=[]
# # for i in range(1000):
# #     t=threading.Thread(target=incerement)
# #     threads.append(t)
# #     t.start()
# # for t in threads:
# #     t.join()
# # print(count)

# '''
# critical section:
# code section where shared resources are accessed is called critical section

# count+=1 ---> critical section

# to avoid the critical section:
# with the help of lock we can avoid the critical section

# one thread should enter the critical section at a time
# solution:
# Lock

# what is a lock?
# synchronisation mechanism that allows 
# only one thread to execute a critical section at a time.

# Thread A acquires Lock
# other threads will wait
# Thread A releases lock
# next thread gets lock

# import threading
# lock= threading.Lock()

# lock.acquire() ---> to apply the lock
# lock.release() ---> to release the lock

# '''
# #example using lock:
# # import threading
# # count=0
# # lock=threading.Lock()
# # def increment():
# #     global count
# #     for i in range(10000):
# #         lock.acquire()
# #         #critical section
# #         count+=1
# #         lock.release()
# # t1=threading.Thread(target=increment)
# # t2=threading.Thread(target=increment)
# # t1.start()
# # t2.start()
# # t1.join()
# # t2.join()
# # print(count)

# '''
# import threading
# count=0
# lock=threading.Lock()
# def increment():
#     global count
#     for i in range(10000):
#         with lock:
#         #critical section
#           count+=1
# t1=threading.Thread(target=increment)
# t2=threading.Thread(target=increment)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(count)
# '''
# #Bank example:
# #without threads
# # class Bank:
# #     def __init__(self):
# #         self.balance = 1000
# #     def withdraw(self,amount):
# #         if self.balance >= amount:
# #             self.amount -= amount
# # import threading
# # lock=threading.Lock()
# # class Bank:
# #     def __init__(self):
# #        self.balance = 1000
# #        self.lock = threading.Lock()
# #     def withdraw(self,amount):
# #             # lock.acquire()
# #         with lock:
# #             if self.balance >= amount:
# #                 self.balance -= amount
# #                 print(amount,"withdraw")
# #             else:
# #                 print("insufficient balance")
# #             # lock.release()
# # bank = Bank()
# # t1=threading.Thread(target=bank.withdraw,args=(700,))
# # t2=threading.Thread(target=bank.withdraw,args=(500,))
# # t1.start()
# # t2.start()
# # t1.join()
# # t2.join()
# # print(bank.balance)

# '''
# Deadlock:
# where the thread wait forever for locks
# Thread 1
# Lock A
# waiting for Lock B

# Thread 2
# Lock B
# Waiting for Lock A

# Thread 1 ---> waiting for Lock A
# Thread 2 ---> waiting for Lock B

# deadlock

# '''
# '''
# Rlock:Recursive lock
# Athread can acquire the same
# lock multiple times

# why Rlock:
# Normal Lock
# acquire once
# release once

# if same thread acquires again
# deadlock


# '''
# # import threading
# # lock=threading.Lock()
# # def outer():
# #     lock.acquire()
# #     inner()
# #     lock.release()
# # def inner():
# #     lock.acquire()
# #     print("Inner")
# #     lock.release()
# # outer()
# '''
# outer()aquired the lock
# inner()trying to acquire the same lock
# lock is already head above
# wait forever
# '''
# # lock=threading.RLock()
# # def inner():
# #     with lock:
# #         print("Inner")
# # def outer():
# #     with lock:
# #         print("Outer")
# #         inner()
# # outer()

# '''
# outer acquire 
# count=1

# inner acquire
# count=2
# inner 

# '''