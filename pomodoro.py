import time

# define the pomodoro timer function
def pomodoro_timer(pomodoro_time, short_break_time, long_break_time, rounds):
    for i in range(rounds):
        print(f"\nRound {i+1} of {rounds}")
        
        # start the pomodoro timer
        print(f"Pomodoro {i+1}: Work for {pomodoro_time} minutes")
        time.sleep(pomodoro_time * 60)  # convert to seconds
        
        # take a short break
        print(f"Take a {short_break_time} minute break")
        time.sleep(short_break_time * 60)  # convert to seconds
        
        # take a long break every fourth round
        if i % 4 == 3:
            print(f"Take a {long_break_time} minute break")
            time.sleep(long_break_time * 60)  # convert to seconds
    
    print("\nGreat job! You've completed your pomodoro sessions.")

# define the main function to get user input and start the timer
def main():
    pomodoro_time = int(input("Enter the duration of each pomodoro session (in minutes): "))
    short_break_time = int(input("Enter the duration of each short break (in minutes): "))
    long_break_time = int(input("Enter the duration of each long break (in minutes): "))
    rounds = int(input("Enter the number of pomodoro rounds: "))
    
    pomodoro_timer(pomodoro_time, short_break_time, long_break_time, rounds)

# run the main function
if __name__ == '__main__':
    main()