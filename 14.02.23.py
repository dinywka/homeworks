import time

hour = 0
minute = 0
second = 0 
while True:
    second += 1

    if second > 59:
        if minute > 59:
            if hour > 23:
                hour = 0
                minute =0
                second = 0
            else:
                hour += 1
                minute = 0
                second = 0
        minute += 1
        second = 1
    time.sleep(1.0)
    print (f"{hour}:{minute}:{second}")
    
