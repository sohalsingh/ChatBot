import random

# List of potential user greetings and chatbot responses
greetings = ['hello', 'hi', 'hey', 'howdy', 'hola']
responses = ['Hello!', 'Hi there!', 'Greetings!', 'Nice to meet you!']

# List of potential user queries and corresponding chatbot responses
queries = ['property', 'buy', 'sell', 'rent']
property_responses = ['We have a wide range of properties available. How can I assist you?', 
                      'Are you looking for a specific type of property?', 
                      'Tell me more about the property you are interested in.']

buy_responses = ['Sure! What type of property are you looking to buy?', 
                 'Do you have any specific requirements for the property?', 
                 'How soon are you planning to make a purchase?']

sell_responses = ['Great! Could you provide more details about the property you want to sell?', 
                  'Are you looking to sell a residential or commercial property?', 
                  'What is the approximate size of the property?']

rent_responses = ['Sure! What type of property are you looking to rent?', 
                  'Do you have any specific requirements for the rental property?', 
                  'How long are you planning to rent the property?']

# Function to generate a chatbot response
def generate_response(message):
    if message.lower() in greetings:
        return random.choice(responses)
    elif 'property' in message.lower():
        return random.choice(property_responses)
    elif 'buy' in message.lower():
        return random.choice(buy_responses)
    elif 'sell' in message.lower():
        return random.choice(sell_responses)
    elif 'rent' in message.lower():
        return random.choice(rent_responses)
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase or ask a different question?"

# Main program loop
print("Chatbot: Welcome to the real estate website chatbot!")
print("Chatbot: How can I assist you today?")

while True:
    user_input = input("User: ")
    response = generate_response(user_input)
    print("Chatbot:", response)