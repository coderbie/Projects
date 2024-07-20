import time
import datetime
import playsound

def alarm(hours: int, minutes: int, day=datetime.now().day, month=datetime.now().month, year=datetime.now().year):
    '''
    Takes hours and minutes as input for alarm time and plays sound when time hits, using playsound library.
    Day, month and year have default values.
    '''
    target_time = datetime(year, month, day, hours, minutes)
    now = datetime.now()

    duration = (target_time-now).seconds

    while True:
        if duration <=0:
            print("Ring......")
            playsound.playsound('alarm_audio.wav')
            break
        duration -=1
        time.sleep(1)
