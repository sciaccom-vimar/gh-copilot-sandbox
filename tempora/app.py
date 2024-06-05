
from typing import List

def calculate_clocktime_difference(clocktower:str, clock_times:str) -> List[int]:
    # implementa la funzione
    clock_time_difference = []
    for time in clock_times:
        hours, minutes = map(int, clocktower.split(':'))
        time_hours, time_minutes = map(int, time.split(':'))
        difference = (time_hours - hours) * 60 + (time_minutes - minutes)
        clock_time_difference.append(difference)
    return clock_time_difference


def main():

    clocktower = "15:00"
    valori = ["14:45", "15:05", "15:00", "14:40"]

    # chiama la funzione calculate_clocktime_difference e fai un output
    clock_time_difference = calculate_clocktime_difference(clocktower, valori)
    print(clock_time_difference)
    

main()