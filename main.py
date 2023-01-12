# Create a Quiz Python
# Variables
total = 0

print("WELCOME TO THE MACBETH QUOTE QUIZ")

# Question Input 1
q1 = input("\n1. Who said 'What, you egg!/ Young fly of treachery!'? ")
print("Q1 Answer: A Murderer")
if q1.lower() == "murderer" or q1.lower() == "a murderer" or q1.lower() == "muderers":
    # Output
    print("Correct")
    total += 1
else:
    print("Incorrect")

# Question Input 2
q2 = input("\n2. Who said 'The queen, my lord, is died.'? ")
print("Q2 Answer: Seyton")
if q2.lower() == "seython" or q2.lower() == "macbeth's servant" or q2.lower() == "satan":
    # Output
    print("Correct")
    total += 1
else:
    print("Incorrect")

# Question Input 3
q3 = input("\n3. Who is 'Turn, hell-hound, turn' refering to? ")
print("Q3 Answer: Macbeth")
if q3.lower() == "macbeth" or q3.lower() == "the tyrant" or q3.lower() == "tyrant":
    # Output
    print("Correct")
    total += 1
else:
    print("Incorrect")

# Question Input 4
q4 = input("\n4. Who was Macbeth written by? ")
print("Q4 Answer: William Shakespear")
if q4.lower() == "shakespear" or q4.lower() == "william" or q4.lower() == "william shakespear":
    # Output
    print("Correct")
    total += 1
else:
    print("Incorrect")

print("\nYOUR RESULTS:")
print(str(total) + "/ 4 (" + str(int(total/4*100)) + "%)")
if total == 0:
    print("Time to study!!")
elif total == 1:
    print("More knowledge = Higher Marks, sometimes")
elif total == 2:
    print("Good Luck next time!")
elif total == 3:
    print("So very close, you'll get it next time")
elif total == 4:
    print("Good Job!")
