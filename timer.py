import winsound
import time
500
def countdown(user_time):
   while user_time >= 0:
       mins, secs = divmod(user_time, 60)
       timer = '{:02d}:{:02d}'.format(mins, secs)
       print(timer, end='\r')
       time.sleep(1)
       user_time -= 1
   print('Timer over')
   winsound.Beep(2000,2000)



if __name__ == '__main__':
   user_time = int(input("Enter a time in seconds: "))
   countdown(user_time)
