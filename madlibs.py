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
    while len(name) < 2:
        name = input('Type a name: ').strip()
    while len(object1) < 2:
        object1 = input('Type a noun: ').strip()   
    while len(descriptive_word) < 2:
        descriptive_word = input('Type an adjective (feeling) : ').strip() 
    while len(verb) < 2:
        verb = input('Type a verb: ').strip()        
    while len(descriptive_word2) < 2:
        descriptive_word2 = input('Type an adjective (feeling): ').strip()
    while len(animal) < 2:
        animal = input('Type an animal: ').strip()     
    while len(verb2) < 2:
        verb2 = input('Type a verb: ').strip()
    while len(color) < 2:
        color = input('Type a color: ').strip()        
    while len(verb3) < 2:
        verb3 = input('Type a verb: ').strip()       
    while len(adverb) < 2:
        adverb = input('Type an adverb(ending in ly): ').strip() 
    while len(number) < 2:
        number = input('Type a number: ').strip()
    while len(measure_of_time) < 2:
        measure_of_time = input('Type a measure of time: ').strip()  
    while len(color2) < 2:
        color2 = input('Type a color: ').strip()  
    while len(animal2) < 2:
        animal2 = input('Type an animal: ').strip()
    while len(number2) < 2:
        number2 = input('Type a number: ').strip()
    while len(silly_word) < 2:
        silly_word = input('Type a silly word: ').strip()      
    while len(object2) < 2:
        object2 = input('Type a noun: ').strip()      

                  
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
    while len(number) < 2:
        number = input('Type a number: ').strip()
    while len(measure_of_time) < 2:
        measure_of_time = input('Type a measure of time: ').strip()    
    while len(transportation_mode) < 2:
        transportation_mode = input('Type a mode of transport: ').strip()  
    while len(descriptive_word) < 2:
        descriptive_word = input('Type an adjective: ').strip()      
    while len(descriptive_word2) < 2:
        descriptive_word2 = input('Type an adjective: ').strip()  
    while len(object1) < 2:
        object1 = input('Type a noun: ').strip()
    while len(color) < 2:
        color = input('Type a color: ').strip()   
    while len(part_of_body) < 2:
        part_of_body = input('Type a body part: ').strip()     
    while len(verb) < 2:
        verb = input('Type an verb: ').strip()
    while len(number2) < 2:
        number2 = input('Type a number: ').strip()
    while len(object2) < 2:
        object2 = input('Type a noun: ').strip()
    while len(object3) < 2:
        object3 = input('Type a noun: ').strip()
    while len(part_of_body2) < 2:
        part_of_body2 = input('Type a body part: ').strip()
    while len(verb2) < 2:
        verb2 = input('Type a verb: ').strip() 
    while len(object4) < 2:
        object4 = input('Type a noun: ').strip()  
    while len(descriptive_word3) < 2:
        descriptive_word3 = input('Type an adjective: ').strip()     
    while len(silly_word) < 2:
        silly_word = input('Type a silly_word: ').strip()
    while len(object5) < 2:
        object5 = input('Type a noun: ').strip()    

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
    while len(name) < 2:
        name = input('Type a name: ').strip()
    while len(number) < 2:
        number = input('Type a number: ').strip()    
    while len(descriptive_word4) < 2:
        descriptive_word4 = input('Type an adjective : ').strip()  
    while len(color3) < 2:
        color3 = input('Type a color: ').strip()      
    while len(object6) < 2:
        object6 = input('Type a noun: ').strip()  
    while len(food_type) < 2:
        food_type = input('Type a type of food: ').strip()
    while len(clothing_article) < 2:
        clothing_article = input('Type a type of clothe: ').strip()   
    while len(descriptive_word5) < 2:
        descriptive_word5 = input('Type an adjective: ').strip()     
    while len(celebrity) < 2:
        celebrity = input('Type a celebrity: ').strip()
    while len(number2) < 2:
        number2 = input('Type a number: ').strip()
    while len(name2) < 2:
        name2 = input('Type a name: ').strip()
    while len(occupation1) < 2:
        occupation1 = input('Type an occupation: ').strip()
    while len(name3) < 2:
        name3 = input('Type a name: ').strip()


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


   










