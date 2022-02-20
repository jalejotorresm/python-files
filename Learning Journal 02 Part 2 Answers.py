#This function will calculate how long a truck will take in hours to deliver a load 
#The calculation will be based on the distance between the shipper and the receiver
#The formula is based on the US Hours Of Service regulations

def transit_tracker(miles):

    transit1=(24*miles)/500 #This line illustrates the value assignment to a variable
    transit2=(24*miles)/600 #This line illustrates the use of simple math equations that interact with the argument of the function

    def min_time(transit2):
        time=transit2

        days=(time//24)
        hours=int(time)
        minutes=(time*60)%60
        seconds=(time*3600)%60

        print('%d day(s), %d hours, %02d minutes and %02d seconds'%(days, hours, minutes, seconds))

    def max_time(transit1):
        time=transit1

        days=(time//24)
        hours=int(time)
        minutes=(time*60)%60
        seconds=(time*3600)%60

        print('%d day(s), %d hours, %02d minutes and %02d seconds'%(days, hours, minutes, seconds))

    print('Minimum amount of time taken:')
    min_time(transit2)

    print('Maximum amount of time taken:')
    max_time(transit1)

    print()

print('Transit Calculator for Loads within the US')
print()

print('Calculation for a load of 310 miles')
transit_tracker(310) #Calcutation made for a load of 310 miles

print('Calculation for a load of 800 miles')
transit_tracker(800) #Calcutation made for a load of 800 miles

print('Calculation for a load of 2560 miles')
transit_tracker(2560) #Calcutation made for a load of 2560 miles

