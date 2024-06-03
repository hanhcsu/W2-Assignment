#Ask the user for the time now (in hours):
now = int(input("Please enter your current time (in hours):"))
while now > 23:
    print("Please enter a valid time which should be less than 24.")
    now = int(input("Please enter your current time (in hours):"))
#Ask for the number of hours to wait for the alarm:
wait = int(input("Please enter the number of hours to wait:"))
#Calculate the alarm time:
alarm = (now + wait) % 24
#Output what the time will be on a 24-hour clock when the alarm goes off.
print(f"The time on a 24-hour clock when the alarm goes off will be {alarm}.")