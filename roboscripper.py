import pyttsx3

if __name__ == '__main__':
    print("welcome to robospeaker 1.1")


    engine = pyttsx3.init()

    while True:
        print("Enter q to stop the program")
        x = input("enter what you want to pronounce: ")
        if x == "q":
            break


        engine.say(x)
        engine.runAndWait()
        
print("Thank You")
