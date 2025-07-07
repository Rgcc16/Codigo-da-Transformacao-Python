import datetime # Import the datetime library

# Ask the user for their name
name = input("Qual é o seu nome? ")

# Get the current time
current_time = datetime.datetime.now().strftime("%H:%M:%S") # Formats time as HH:MM:SS

# Create the personalized greeting message including the time
message = (f"Olá, { name } ! Bem-vindo(a)! A hora atual é {current_time} .")

# Display the message
print(message)