def madlib():
    """ Asks the user for input, validates the input and returns the string"""
    # User input variables
    name = ""
    valid_name = False 
    while valid_name is False:
        name = input('Please enter a name:')
        if get_validated_input(100, 2, name):
            name.capitalize()
            valid_name = True
        else:
            get_validated_input(100, 2, name)
    object1 = ""
    valid_object1 = False 
    while valid_object1 is False:
        object1 = input('Please enter a noun:')
        if get_validated_input(100, 2, object1):
            valid_object1 = True
        else:
            get_validated_input(100, 2, object1)
    descriptive_word = ""
    valid_descriptive_word = False 
    while valid_descriptive_word is False:
        descriptive_word = input('Please enter an adjective:')
        if get_validated_input(100, 2, descriptive_word):
            valid_descriptive_word = True
        else:
            get_validated_input(100, 2, descriptive_word)
    verb = ""
    valid_verb = False
    while valid_verb is False:
        verb = input('Please enter a verb:')
        if get_validated_input(100, 2, verb):
            valid_verb = True
        else:
            get_validated_input(100, 2, verb)
    descriptive_word2 = ""
    valid_descriptive_word2 = False 
    while valid_descriptive_word2 is False:
            descriptive_word2 = input('Please enter an adjective:')
        if get_validated_input(100, 2, descriptive_word2):
            valid_descriptive_word2 = True
        else:
            get_validated_input(100, 2, descriptive_word2) 
    animal = ""
    valid_animal = False 
    while valid_animal is False:
        animal = input('Please enter an animal:')
        if get_validated_input(100, 2, animal):
            valid_animal = True
        else:
            get_validated_input(100, 2, animal)
    verb2 = ""
    valid_verb2 = False 
    while valid_verb2 is False:
        verb2 = input('Please enter a verb:')
        if get_validated_input(100, 2, verb2):
            valid_verb2 = True
        else:
            get_validated_input(100, 2, verb2)
    color = ""
    valid_color = False 
    while valid_color is False:
        color = input('Please enter a color:')
        if get_validated_input(100, 2, color):
            valid_color = True
        else:
            get_validated_input(100, 2, color)
    # make this verb end in ing
    verb3 = ""
    valid_verb3 = False 
    while valid_verb3 is False:
        verb3 = input('Please enter a verb:')
        if get_validated_input(100, 2, verb3):
            valid_verb = True
        else:
            get_validated_input(100, 2, verb3)
    # this adverb has to end in ly
    adverb = ""
    valid_adverb = False 
    while valid_adverb is False:
        adverb = input('Please enter an adverb (ending in ly):')
        if get_validated_input(100, 2, adverb):
            valid_adverb = True
        else:
            get_validated_input(100, 2, adverb)
    number = validate_number()
    measure_of_time = ""
    valid_measure_of_time = False 
    while valid_measure_of_time is False:
        measure_of_time = input('Please enter a measure of time:')
        if get_validated_input(100, 2, measure_of_time):
            valid_measure_of_time = True
        else:
            get_validated_input(100, 2, measure_of_time)    
    color2 = ""
    valid_color2 = False 
    while valid_color2 is False:
        color2 = input('Please enter a color:')
        if get_validated_input(100, 2, color2):
            valid_color2 = True
        else:
            get_validated_input(100, 2, color2)
    animal2 = ""
    valid_animal2 = False 
    while valid_animal is False:
        animal2 = input('Please enter an animal:')
        if get_validated_input(100, 2, animal2):
            valid_animal2 = True
        else:
            get_validated_input(100, 2, animal2)
    number2 = validate_number()
    silly_word = ""
    valid_silly_word = False
    while valid_silly_word is False:
        silly_word = input('Please enter a silly word:')
        if get_validated_input(100, 2, silly_word):
            valid_silly_word = True
        else:
            get_validated_input(100, 2, silly_word)
    object2 = ""
    valid_object2 = False 
    while valid_object2 is False:
        object2 = input('Please enter a noun:')
        if get_validated_input(100, 2, object2):
            valid_object2 = True
        else:
            get_validated_input(100, 2, object2)

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
    print(first_madlib)
          
def madlib_2():
    """ Asks the user for input, validates the input and returns the string"""
    # User input variables
    number = validate_number()
    measure_of_time = ""
    valid_measure_of_time = False 
    while valid_measure_of_time is False:
        measure_of_time = input('Please enter a measure of time:')
        if get_validated_input(100, 2, measure_of_time):
            valid_measure_of_time = True
        else:
            get_validated_input(100, 2, measure_of_time)
    transportation_mode = ""
    valid_transportation_mode = False 
    while valid_transportation_mode is False:
        transportation_mode = input('Please enter a transportation mode:')
        if get_validated_input(100, 2, transportation_mode):
            valid_measure_of_time = True
        else:
            get_validated_input(100, 2, transportation_mode)
    descriptive_word = ""
    valid_descriptive_word = False 
    while valid_descriptive_word is False:
            descriptive_word = input('Please enter an adjective:')
        if get_validated_input(100, 2, descriptive_word):
            valid_descriptive_word = True
        else:
            get_validated_input(100, 2, descriptive_word)
    descriptive_word2 = ""
    valid_descriptive_word2 = False
    while valid_descriptive_word2 is False:
            descriptive_word2 = input('Please enter an adjective:')
        if get_validated_input(100, 2, descriptive_word2):
            valid_descriptive_word2 = True
        else:
            get_validated_input(100, 2, descriptive_word2)
    object1 = ""
    valid_object1 = False
    while valid_object1 is False:
        object1 = input('Please enter a noun:')
        if get_validated_input(100, 2, object1):
            valid_object1 = True
        else:
            get_validated_input(100, 2, object1)
    color = ""
    valid_color = False 
    while valid_color is False:
        color = input('Please enter a color:')
        if get_validated_input(100, 2, color):
            valid_color = True
        else:
            get_validated_input(100, 2, color)
    part_of_body = ""
    valid_part_of_body = False
    while valid_part_of_body is False:
        part_of_body = input('Please enter a body part:')
        if get_validated_input(100, 2, part_of_body):
            valid_part_of_body = True
        else:
            get_validated_input(100, 2, part_of_body)
    verb = ""
    valid_verb = False
    while valid_verb is False:
        verb = input('Please enter a verb:')
        if get_validated_input(100, 2, verb):
            valid_verb = True
        else:
            get_validated_input(100, 2, verb)
    number2 = validate_number()
    object2 = ""
    valid_object2 = False
    while valid_object2 is False:
        object2 = input('Please enter a noun:')
        if get_validated_input(100, 2, object2):
            valid_object2 = True
        else:
            get_validated_input(100, 2, object2)
    object3 = ""
    valid_object3 = False
    while valid_object3 is False:
        object3 = input('Please enter a noun:')
        if get_validated_input(100, 2, object3):
            valid_object3 = True
        else:
            get_validated_input(100, 2, object3)
    part_of_body2 = ""
    valid_part_of_body2 = False 
    while valid_part_of_body2 is False:
        part_of_body2 = input('Please enter a body part:')
        if get_validated_input(100, 2, part_of_body2):
            valid_part_of_body2 = True
        else:
            get_validated_input(100, 2, part_of_body2)
    verb2 = ""
    valid_verb2 = False 
    while valid_verb2 is False:
        verb2 = input('Please enter a verb:')
        if get_validated_input(100, 2, verb2):
            valid_verb2 = True
        else:
            get_validated_input(100, 2, verb2)
    object4 = ""
    valid_object4 = False
    while valid_object4 is False:
        object4 = input('Please enter a noun:')
        if get_validated_input(100, 2, object4):
            valid_object4 = True
        else:
            get_validated_input(100, 2, object4)
    descriptive_word3 = ""
    valid_descriptive_word3 = False
    while valid_descriptive_word3 is False:
            descriptive_word3 = input('Please enter an adjective:')
        if get_validated_input(100, 2, descriptive_word3):
            valid_descriptive_word3 = True
        else:
            get_validated_input(100, 2, descriptive_word3)
    silly_word = ""
    valid_silly_word = False 
    while valid_silly_word is False:
        silly_word = input('Please enter a silly word:')
        if get_validated_input(100, 2, silly_word):
            valid_silly_word = True
        else:
            get_validated_input(100, 2, silly_word)
    object5 = ""
    valid_object5 = False
    while valid_object5 is False:
        object5 = input('Please enter a noun:')
        if get_validated_input(100, 2, object5):
            valid_object5 = True
        else:
            get_validated_input(100, 2, object5)
 
    second_madlib = f'''
    It was about {number} {measure_of_time} ago when I came to 
    the hospital in a {transportation_mode}. The hospital is a 
    {descriptive_word} place, there are a lot of {descriptive_word2} 
    {object1} here. There are nurses here who have {color} {part_of_body}. 
    If someone wants to come into my room I told them that they have to 
    {verb} first.I have decorated my room with {number2} {object2}. 
    Today a doctor came into my room and they were wearing a 
    {object3} on their {part_of_body2}. I heard that all doctors 
    {verb2} {object4} everyday for breakfast. The most {descriptive_word3} 
    thing about being in the hospital is the {silly_word} {object5}.
    '''

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


   










