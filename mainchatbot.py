import datetime
tour_responses = {
    "hi": "Hello! How can I assist you with your tour?",
    "hello": "Hi there! How can I help you today?",
    "book a tour": "Sure, where would you like to go?",
    "available tours": "We offer tours to various destinations. What place are you interested in?",
    "tour packages": "We have various packages. Where would you like to travel?",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome!",
    "help": "I'm here to assist you with your tour. What do you need help with?",
    "destinations": "We offer tours to various destinations including Paris, Tokyo, New York, Rome, and Bali. Which destination are you interested in?",
    "paris": "Paris, the city of lights, offers iconic landmarks like the Eiffel Tower and Louvre Museum. What specific information do you need about Paris?",
    "tokyo": "Tokyo is a vibrant metropolis blending tradition and modernity. Are you interested in learning about Tokyo's attractions or cultural experiences?",
    "new york": "New York City is known for its bustling streets, Central Park, and Broadway shows. What details would you like to know about New York?",
    "rome": "Rome, the Eternal City, boasts ancient ruins and historic sites like the Colosseum and Vatican City. What interests you about Rome?",
    "bali": "Bali offers beautiful landscapes, serene beaches, and cultural richness. What information are you seeking about Bali?",
    "cost": "The cost varies based on the destination and package. Could you specify your preferences?",
    "time": "The duration of tours can vary. Do you have a specific time frame in mind?",
    "activities": "Our tours offer a range of activities such as sightseeing, hiking, and cultural experiences. What activities interest you?",
    
    "food": "Meals are provided during the tour. Do you have any dietary preferences or restrictions?",
    "group size": "Our tours accommodate different group sizes. How many people will be joining the tour?",
    "age limit": "Age restrictions may apply to certain tours. Could you provide the age range of participants?",
    "custom tour": "We can create a custom tour based on your preferences. What specific requirements do you have?",
    "special offers": "We occasionally have special offers and discounts. Is there a particular offer you're interested in?",
    "refund policy": "Our refund policy depends on the tour package. Would you like more details about a specific tour's refund policy?",
    "contact": "You can reach our customer service at customer_service@example.com or call us at +123456789.",
    "tour duration": "The duration of the tour varies depending on the package and destination.",
    "tourist attractions": "There are several popular tourist attractions at our destinations. Are you looking for information about specific attractions?",
    "weather": "The weather at our destinations can vary. Do you want to know the weather forecast for a particular location?",
    "itinerary": "We provide a detailed itinerary for each tour package. Would you like to see the itinerary for a specific tour?",
    "reviews": "Our customers have provided positive reviews for our tours. Would you like to read some testimonials?",
    "solo traveler": "We have tours suitable for solo travelers. Would you prefer a tour designed for individuals?",
    "family-friendly": "Many of our tours are family-friendly with activities suitable for all ages. Are you planning a family trip?",
    "emergency contact": "We provide emergency contact details for each tour. Is there anything specific you'd like to know about emergency contacts?",
    "language options": "We offer tours in multiple languages. Do you have a preferred language for the tour guide?",
    "sightseeing tours": "We have sightseeing tours available at various destinations. Would you like to explore sightseeing options?",
    "cultural experiences": "Our tours often include cultural experiences. Are you interested in immersing yourself in the local culture?",
    "adventure tours": "For adventure enthusiasts, we offer exciting adventure tours. Are you seeking an adventurous experience?",
    "cancellation policy": "Cancellation policies differ based on the tour package and timing. Would you like information on a specific tour's cancellation policy?",
    "payment methods": "We accept various payment methods including credit/debit cards and bank transfers. How would you prefer to make payment?",
    "tour guide availability": "Tour guides are available for most of our tours. Would you like to have a tour guide?",
    "online booking": "You can book tours online through our website. Do you need assistance with the online booking process?",
    "local cuisine": "Our tours often include experiences with local cuisine. Are you curious about the food options?",
    "health precautions": "We take health precautions seriously. Is there anything specific you'd like to know about health and safety measures during the tour?",
    "photography opportunities": "There are numerous photography opportunities during our tours. Are you interested in photography?",
    "sustainable tourism": "We promote sustainable tourism practices. Would you like to know more about our efforts in sustainable tourism?",
    "lost items": "We have a procedure for handling lost items during tours. Is there anything specific you'd like to inquire about lost items?",
    "previous experience": "Have you been on similar tours before? Your previous experience can help us tailor recommendations for you.",
    "calculated tour duration" : "Enter tour start date (YYYY-MM-DD): "
}


def calculate_tour_duration(start_date, end_date):
    try:
        start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        duration = end - start
        return duration.days  # Return the duration in days
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD format for dates."

# Function to handle user input and provide responses
def tour_chatbot(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for case-insensitive matching
    for pattern, response in tour_responses.items():
        if pattern in user_input:
            return response
    return "I'm sorry, I didn't understand that. Can you please be more specific?"

# Interactive loop to simulate chatbot interaction
print("Welcome to the Tour Management Chatbot")
print("Type 'bye' to exit")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print(tour_chatbot('bye'))  # Display goodbye message
        break
    elif user_input.lower() == 'calculate tour duration':
        start_date_input = input("Enter tour start date (YYYY-MM-DD): ")
        end_date_input = input("Enter tour end date (YYYY-MM-DD): ")

        tour_duration = calculate_tour_duration(start_date_input, end_date_input)
        if isinstance(tour_duration, int):
            print(f"The tour duration is {tour_duration} days.")
        else:
            print(tour_duration)
    else:
        bot_response = tour_chatbot(user_input)
        print("Bot:", bot_response)