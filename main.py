# Data Collection Drills


#Part A: Lists
my_list = ["M", "A", "C", "H", "I", "N", "E"]
print(my_list) #["M", "A", "C", "H", "I", "N", "E"]
my_list.append("!") # added a ! There was not a ! before, then it was added to the end
print(my_list)
print(len(my_list))#8
print(my_list[4:6]) # It returned the letters 4 through 6. It works because  those numbers exist in the list, if they didn't, it wouldn't work
print(my_list[4:]) #It returned letter 4 till it stopped. No it is not the same as above.
print(my_list[-2:]) # It returned the last two letters It is useful because you can check if the list works
my_list.remove("!") 
print(my_list) # The ! was removed. It finds where it is and takes it out
my_list.insert(2, "l") #It went exactly where instructed to. l is at index two
print(my_list)
del my_list[0]
print(my_list) #The letter in index 1
last_item = my_list.pop() #
print(last_item)
print(my_list)
print("!" in my_list)
my_list.sort(reverse=True)
print(my_list)
print(sorted(my_list))
print(my_list)
# Part B: Tuples
my_tuple = ("red", "green", "bleen")
print(my_tuple)
print(my_tuple[0])
print(my_tuple[-1])


# my_tuple[1] = "yellow"


# What do you notice about the syntax?


# Part C: Sets


# Part D: Dictionaries
