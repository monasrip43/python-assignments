'''
loop control:

Break: it stops the execution of the loop immediately
(terminates the loop immediately)

Continue : skips the current iteration

Pass : do's nothing

'''

#example break
'''
i = 1
while i<=10:
       if i == 5:
              break  #terminates at 5
       print(i)
       i += 1
'''
#continue : skips the current iteration (given condition) and moves to the next iteration
'''
for i in range(1,11):
       if i == 5:
              continue
       print(i)
       '''
##pass : do's nothing provides the placeholder for the code
'''
for i in range(1,11):
  pass #if pass is not used it shows the error in the code
  '''
#if pass is used the code doesnt show any error and also doesnt have any change in the code
# example to use all the break,pass and continue
'''
for i in range(1,11):
    pass
    if i==2:
        continue
    if i==5:
        break
    print(i)
    '''

#Summary
'''
difference between for and while

for: used for when the iterations are known
best for iterating over the sequences
 
while: it is used when the iterations are unknown
best condition controlled loops
best for condition based repetition
it executes until the condition is true

2. what makes the loop infinite
 if the given condition never mets false becomes an infinite loop
        (or)
missing of increment and decrement in the loop


3. can we use else with while
    i = 1
    while i<=3:
    print(i)
   else:
      print("loop is finished")
Note: Else wont work if there is a break statement

      '''
