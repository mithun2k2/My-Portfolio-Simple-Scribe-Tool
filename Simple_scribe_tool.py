text = '''  Hi 
            I'm here: 
            London
            UK
            USA 
            Where are you:
            Here
            There
            What will you do:
            Go back
            Returning something '''

# add ';'  if there is ':' else insert the line

output = [line.strip() if ':' not in line else ';' for line in text.split('\n')]

# Join the list on space

output = ' '.join(output)

# Split back in list on ',' and trim the white spaces

output = [item.strip() for item in output.split(';')]

print(output)

replaced_text = text.replace('London', 'Newyork')
print(replaced_text)

# Open up a text file storing in variable
file_path = "passenger_data.txt"

# promt user for the data input
user_input = int(input("Please enter the number of passengers: "))

passenger_list = " "

with open(file_path, "w") as file:
    
    for i in range(0, user_input):
# promt passenger to enter their name:
        passenger_list = input(" Please enter each passenger name: ")

        file.write(passenger_list + "\n")


print("Thank you, Passengers data saved to txt file passenger_data")


