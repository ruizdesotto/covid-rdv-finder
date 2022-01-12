import winsound
import time

FREQUENCY = 2000  # Set Frequency To 2500 Hertz
DURATION = 500  # Set Duration To 1000 ms == 1 second
WAIT_DURATION = 0.25

def beep(num = 3):
    for _ in range(num):
        winsound.Beep(FREQUENCY, DURATION)
        time.sleep(WAIT_DURATION)

if __name__ == "__main__":
    beep()