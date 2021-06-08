import time


def word_repeater():
    '''Function to do Word Repeater'''
    word = input("Enter Which Word You'd Like to Repeat\n")
    times = input(f"Enter How Many Times You'd Like to Repeat '{word}' as an integer.\n")
    i_times = int(times)
    ticker = 0
    while ticker < i_times:
        count = ticker + 1
        print(f"{count}." + f" {word}\n")
        ticker = ticker + 1
        time.sleep(0.1)
    print("All Done!")
    def do_again():
        """Function to repeat or exit program"""
        again = input("Press 1 to do again, Press 2 to Exit.\n")
        if again == "1":
            word_repeater()
        elif again == "2":
            exit()
        else:
            input("Invalid response, press enter to try again.\n")
            do_again()
    do_again()
word_repeater()
