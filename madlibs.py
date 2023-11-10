def madlib():
    """ Asks the user for input, validates the input and returns the string"""
    # User input variables
    name = ""
    object1 = ""
    descriptive_word = ""
    verb = ""
    descriptive_word2 = ""
    animal = ""
    verb2 = ""
    color = ""
    # make this verb end in ing
    verb3 = ""
    # this adverb has to end in ly
    adverb = ""
    number = ""
    measure_of_time = ""
    color2 = ""
    animal2 = ""
    number2 = ""
    silly_word = ""
    object2 = ""

    # Checking user input
    name = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a name:')
    object1 = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a noun:')
    descriptive_word = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a noun:')
    verb = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a verb:')
    descriptive_word2 = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a noun:')
    animal = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter an animal:')    
    verb2 = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a verb:')
    color = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a color:')     
    verb3 = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a verb:')     
    adverb = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a verb:')
    number = ValidateNumber()
    measure_of_time = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a measure of time:') 
    color2 = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a color:')  
    animal2 = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter an animal:')
    number2 = ValidateNumber()
    silly_word = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a silly word:')     
    object2 = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a noun:')
 

                  
    first_madlib = f'''
    This weekend I am going camping with {name}.
    I packed my lantern, sleeping bag, and {object}.
    I am so {descriptive_word} to {verb} in a tent. 
    I am {descriptive_word2} we might see a {animal}, they are kind of 
    dangerous. We are going to hike, fish, and {verb2}. 
    I have heard that the {color} lake is great for
    {verb3}. Then we will {adverb} hike through the forest for {number} 
    {measure_of_time}. If I see a {color2} {animal2} while hiking,
    I am going to bring it home as a pet!  At night we will tell 
    {number2}{silly_word}stories and roast {object2} around the fire'''

def ValidateNumber():
    while True:
        user_input = input('Type a number:')
        try:
            number = int(user_input)
            break
        except ValueError:
            print("Thats's not a valid number. Please try again.")

def get_validated_input(maxStringLength, minStringLength, inputPrompt):
    while True:
        user_input = input(inputPrompt).strip()

        if not (minStringLength < len(user_input) < maxStringLength):
            print("Input length must be more than" + 
                 minStringLength + "and less than" + maxStringLength + "characters")
            continue
        if not all(char.isalnum() for char in user_input):
            print("Input should not contain special characters.")
            continue

        return user_input.lower()           
def madlib_2():
    """ Asks the user for input, validates the input and returns the string"""
    # User input variables
    number = ""
    measure_of_time = ""
    transportation_mode = ""
    descriptive_word = ""
    descriptive_word2 = ""
    object1 = ""
    color = ""
    part_of_body = ""
    verb = ""
    number2 = ""
    object2 = ""
    object3 = ""
    part_of_body2 = ""
    verb2 = ""
    object4 = ""
    descriptive_word3 = ""
    silly_word = ""
    object5 = ""

    # Checking user input
    number = ValidateNumber()
    measure_of_time = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a measure of time:')   
    transportation_mode = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a mode of transport:') 
    descriptive_word = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter an adjective:')       
    descriptive_word2 = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter an adjective:')  
    object1 = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a noun:')
    color = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a color:')  
    part_of_body = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a body part:')     
    verb = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a verb:')
    number2 = ValidateNumber()
    object2 = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a noun:')    
    object3 = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a noun:')    
    part_of_body2 = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a body part:')
    verb2 = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a verb:')
    object4 = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a noun:')    
    descriptive_word3 = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter an adjective:')     
    silly_word = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a silly word:')
    object5 = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a noun:')
 

    second_madlib = f'''It was about {number} {measure_of_time} ago when I came to the hospital in a {transportation_mode}. The hospital is a {descriptive_word}
    place, there are a lot of {descriptive_word2} {object1} here. There are nurses here who have {color} {part_of_body}. If someone wants to come
    into my room I told them that they have to {verb} first.I have decorated my room with {number2} {object2}. Today a 
    doctor came into my room and they were wearing a {object3} on their {part_of_body2}. I heard that all doctors {verb2} {object4} 
    everyday for breakfast. The most {descriptive_word3} thing about being in the hospital is the {silly_word} {object5}.'''

def madlib_3():
    """ Asks the user for input, validates the input and returns the string"""
    #  User input variables
    name = ""
    number = ""
    descriptive_word4 = ""
    color3 = ""
    object6 = ""
    # has to be plural
    food_type = ""
    clothing_article = ""
    descriptive_word5 = ""
    celebrity = ""
    number2 = ""
    name2 = ""
    occupation1 = ""
    name3 = ""

    # Checking user input
    name = get_validated_input(maxStringLength=12, minStringLength=2, inputPrompt='Please enter a name:')
    number = ValidateNumber()  
    descriptive_word4 = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter an adjective:')  
    color3 = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a color:')        
    object6 = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a noun:')  
    food_type = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a food:')
    clothing_article = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a clothing article:')   
    descriptive_word5 = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter an adjective:')     
    celebrity = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter a celebrity:')
    number2 = ValidateNumber()
    name2 = get_validated_input(maxStringLength=12, minStringLength=2, inputPrompt='Please enter a name:')
    occupation1 = get_validated_input(maxStringLength=12, minStringLength=3, inputPrompt='Please enter an occupation:')
    name3 = get_validated_input(maxStringLength=12, minStringLength=2, inputPrompt='Please enter a name:')



    third_madlib = f'''
    My name is {name} and I am {number} years old.
    If I were president, I'd do a whole bunch {descriptive_word4}
    things. I would drive the biggest {color3} car in the country.
    That car would go faster than any other {object6} in the world.
    Everyone would eat {food_type} for dinner. I would wear a {clothing_article}
    on my head and everyone would say I look {descriptive_word5} like
    {celebrity}. School would only be open {number2} years a day.
    I would give my friends the best jobs. I would nominate {name2} to be
    {occupation1} and {name3} could be vice {occupation1}. '''


   










