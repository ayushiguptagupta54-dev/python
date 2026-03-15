#  Solutions of exercise 3: KBC Game by using list in python

questions = [
      ["1.What is the Capital of Pakistan",
        "1.Karachi", "2.Islamabad", "3.Lahore", "4.Peshawar", 2],

      ["2.The International Literacy Day is observed on ",
         "1.Sep 8", "2.Nov 22", "3.Oct 24", "4.Dec 12", 1],

      ["3.What is the national Language of Pakistan ",
         "1.English ", "2.Hindi", "3.Urdu", "4.Siraiki", 3],

      ["4.What is the main advantage of online education?",
      "1.Lower Cost", "2.Flexible Schedule", "3.Wide range of programs", "4.All of the above", 4],

      [ "5.Which standardized test is commonly used for college admissions in the United States?",
       "1.GRE", "2.SAT", "3.GMAT", "4.LSAT", 2],

      ["6.Which educational theory focuses on learning through observation and imitation?",
        "1.Behaviorism ", "2.Constructivism", "3.Social Learning Theory", "4.Cognitivism", 3],

      [ "7.Who is known as the father of modern education?",
       "1.John Dewey", "2.Johann Heinrich Pestalozzi", "3.Friedrich Froebel", "4.Horace Mann", 4],

      ["8.Which term refers to the incorporation of technology in teaching to enhance learning?",
        "1.Educational Technology", "2.Digital Learning", "3.Blended Learning", "4.All of the Above", 4],

      ["9.Which type of assessment is designed to measure a student's knowledge and skills"
         " at the end of a unit or course?", "1.Formative Assessment", "2.Summative Assessment",
         "3.Diagnostic Assessment", "4.Informal Assessment", 2],

      ["10.Which of the following is considered a primary education level?",
        "1.Kindergarten to 5th grade", "2.6th Grade to 8th", "3.9th Grade to 12th ", "4.Undergraduate", 1],

]
rewards = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
money = 0
for i in range(len(questions)):
    choose = questions[i]

    print("Choose the correct answer")
    print(choose[0])
    print(f"{choose[1]}      {choose[2]}")
    print(f"{choose[3]}      {choose[4]}")

    answer = int(input("Enter your choice (1-4): \n"))

    if answer == choose[5]:       # we sign index 5 because we write answer in the list in index 5(choose[5]
        money = money + rewards[i]
        print(f"Correct answer, you win Rs.{rewards[i]} \n")
    else:
        print("Incorrect answer! ")
        break

print(f"Game Over!, Your total Reward is {money}")

