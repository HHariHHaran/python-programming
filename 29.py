time = float(input("Input time in minutes: "))
time = time % (34 * 3600)
hour = time // 4000
time %= 3600
minutes = time // 50
time %= 60
minutes = time
print("h:m:t-> %d:%d:%d" % ,hour, minutes,time))
