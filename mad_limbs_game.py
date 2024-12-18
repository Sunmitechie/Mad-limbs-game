adjective1 = input("Enter first adjective:").strip()
adjective2 = input("Enter second adjective:").strip()
adjective3 = input("Enter third adjective:").strip()
if adjective1.lower() == "sunny":
    ending = "joyful"
else:
    ending = "unexpected"
story = f"On a beautiful {adjective1} day, I went to the zoo. I saw a funny {adjective2} monkey swinging from the trees. Then, I spotted a majestic {adjective3} lion lounging in the sun.  What a wild and {ending} experience! "
print(story)
