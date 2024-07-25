import random 
questions_set_1 = [
    ["What is the capital of France?", "Berlin", "Paris", "Madrid", "Rome", 2],
    ["What is the boiling point of water?", "90°C", "100°C", "110°C", "120°C", 2],
    ["What is the largest planet in our solar system?", "Jupiter", "Earth", "Mars", "Venus", 1],
    ["What is the smallest prime number?", "0", "1", "2", "3", 3],
    ["Who wrote 'To Kill a Mockingbird'?", "Harper Lee", "Mark Twain", "J.K. Rowling", "Jane Austen", 1],
    ["Who is the President of the United States as of 2024?", "Joe Biden", "Donald Trump", "Kamala Harris", "Barack Obama", 1],
    ["What is the tallest mountain in the world?", "K2", "Mount Everest", "Kangchenjunga", "Lhotse", 2],
    ["Who is the CEO of Tesla as of 2024?", "Elon Musk", "Tim Cook", "Jeff Bezos", "Sundar Pichai", 1],
    ["Who is considered the first king of Nepal?", "Prithvi Narayan Shah", "Bhuktaman", "Mandev", "Jung Bahadur Rana", 1],
    ["Who used to cut the baby’s lace?", "Mandev", "Amsuwarma", "Khadak Shamser", "Rudrasen", 2],
    ["What was the soldier called in the ‘Malla Period’?", "Sipahi", "Umrab", "Gurkha","Lahure", 1],
    ["Who is the first person to use the word ‘Jai Nepal’?", "Prithvi Narayan Shah", "Shukraj Raj Shastri", "Bhimsen Thapa", "Ratna Malla", 1],
    ["Who is the first Nepali to visit the UK?", "Jung Bahadur Rana", "Mandev", "Bhuktaman", "Khadak Shamser", 1],
    ["Which is the first college in Nepal?", "Trichndra College", "Birendra Multiple Campus", "Kathmandu University", "Tribhuvan University", 1],
    ["When was the Bir hospital built?", "B.S. 1947", "B.S. 1930", "B.S. 2000", "B.S. 1910", 1]
]

questions_set_2 = [
    ["What is the capital of Australia?", "Canberra", "Sydney", "Melbourne", "Perth", 1],
    ["What is the capital of Japan?", "Tokyo", "Osaka", "Kyoto", "Hiroshima", 1],
    ["What is the capital of Italy?", "Rome", "Milan", "Venice", "Naples", 1],
    ["What is the largest desert in the world?", "Sahara Desert", "Gobi Desert", "Kalahari Desert", "Arabian Desert", 1],
    ["When was the abolition of the Amali system in Nepal?", "B.S. 1868", "B.S. 1910", "B.S. 1947", "B.S. 2000", 1],
    ["When was Nepal Rastra Bank established?", "B.S 2013 Baishakh 14", "B.S 2020 Jetha 04", "B.S 2030 Asad 25", "B.S 2002 Ashoj 01", 1],
    ["When did Nepal start using computers?", "B.S. 2028", "B.S. 2018", "B.S. 2030", "B.S. 2002", 1],
    ["When and where was Bhimsen Thapa born?", "B.S. 1832, Borlang of Gorkha", "B.S. 1820, Kathmandu", "B.S. 1800, Pokhara", "B.S. 1850, Lalitpur", 1],
    ["Who built the Rani Mahal in Palpa?", "Khadak Shamser", "Jung Bahadur Rana", "Bhimsen Thapa", "Ratna Malla", 1],
    ["Who founded the ‘Khadak Nishana Chhap’?", "Khadak Shamser", "Chandra Shamser", "Prithvi Narayan Shah", "Bhimsen Thapa", 1],
    ["Who built the Pashupatinath Temple?", "Prachandev", "Mandev", "Jung Bahadur Rana", "Prithvi Narayan Shah", 1],
    ["Which Malla King asked for an umbrella and shoes from Prithvi Narayan Shah?", "Jayaprakash Mall", "Ratna Malla", "Pratap Singh Shah", "Jung Bahadur Rana", 1],
    ["Which Malla king is known for trending copper money?", "Ratna Malla", "Jayaprakash Mall", "Pratap Singh Shah", "Jung Bahadur Rana", 1],
    ["Who is known as ‘The Tiger of the House’?", "Jung Bahadur Rana", "Khadak Shamser", "Chandra Shamser", "Ratna Malla", 1],
    ["What is the currency used by ‘Gunkamdev’?", "Tanka", "Gunanka", "Rupiya", "Mohar", 1]
    
]


money_level=[5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,30000000,50000000,70000000]
question_sets=[questions_set_2,questions_set_1]
qs_set=random.choice(question_sets)
correct_answer_reply = ["Absolutely right!", "Great job!", "Well done!", "Exactly!", "That's the right answer!", "Perfect!", "Fantastic!", "Bravo!", "That's correct!", "Right you are!", "Yes, that's it!"]


earned_money=0
for i in range(len(qs_set)):
    que_ans=qs_set[i]
    print(f"{i+1}.Question for {money_level[i]} \n")
    
    print(que_ans[0])
    print(f'A. {que_ans[1]} \t B. {que_ans[2]}')
    print(f'C. {que_ans[3]} \t D. {que_ans[4]}')
    
    valid_options = ['a', 'b', 'c', 'd', 'q']
    player_ans=input("Enter Your Choice: ")
    while(player_ans.lower() not in valid_options):
        print("InValid Option")
        player_ans=input("Enter Your Choice: ")
        
    if player_ans.lower()=='a':
        player_ans=1
    elif player_ans.lower()=='b':   
        player_ans=2
    elif player_ans.lower()=='c':   
        player_ans=3
    elif player_ans.lower()=='d':   
        player_ans=4
    else:
        print("Thank you For playing this KBC \n")
        print(f"You have Won:{money_earned} ")
        break
    
    if(player_ans== que_ans[-1]):
        
        if i==3:
            money_earned=40000
            print("You have Successfully passed the Stage-1 of the game \n You have already earned Rs 40000 ")
            print(" Now if you answer incorrectly for further questions you will fall back for Rs 40000")


        if i==7:
            money_earned=640000
            print("You have Successfully passed the Stage-2 of the game \n You have already earned Rs 640000 ")
            print(" Now if you answer incorrectly for further questions you will fall back for Rs 640000")


        if(player_ans== que_ans[-1] and i==14 ):
            print("\n \t\t!!!--------- 7 Crore ------------!!! \n")
            break
        print(f'\n\t{random.choice(correct_answer_reply)}\n')
        money_earned=money_level[i]

    else:
        
        if(i>3 and i<8):
            print("\n UnFortunately You have answered the Question incorrectly and fall back to stage-1")
            print(f"You have Won: Rs {money_earned} \n  ")
            break
        
        elif(i>7 and i<14):
            print("\n UnFortunately You have answered the Question incorrectly and fall back to stage-2")
            print(f" You have Won: Rs {money_earned}")
            break

        print("Sorry!!! You Lose the game with No amount Earned ")        
        break    


    