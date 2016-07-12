import time
timerm = float(input ("How long do you want to time for in minutes"))
timers = timerm * 60
while timers != 0:
  print (timers)
  timers = timers - 1
  time.sleep(1)
for x in range (50):
    print ("TIMER FINISHED")
    time.sleep(0.4)
    print ("TIMER FINISHED")
    time.sleep(0.4)
    print ("TIMER FINISHED\n\n")
    time.sleep(0.8)
