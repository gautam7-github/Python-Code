print("TYPE SOMETHING TO CHAT WITH JARVIS : ")

hi_list = ['hello', 'hi', 'namaste']
ask_list = ['how are you?', 'how are you doing?', 'what is going on?', 'are you ok?']
resp_list = ['great', 'good', 'top notch', 'awesome']
while True:
    inp = input()
    for i in hi_list:
        if inp == i:
            print("HELLO THERE")
    for i in ask_list:
        if inp == i:
            print("I am Fine")
            print("HOW ARE YOU?")
            inp_res = input()
            for check_res in resp_list:
                if inp_res == check_res:
                    print("GOOD TO HEAR THAT....")
