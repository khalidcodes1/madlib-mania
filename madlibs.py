def madlib():
    """ Asks the user for input, validates the input and returns the string"""
    # User input variables
    proper_noun = ""
    noun = ""
    adjective = ""
    verb = ""
    adjective2 = ""
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
    noun2 = ""

    # Checking user input
    while len(proper_noun) < 2:
        proper_noun = input('Type a proper noun: ').strip()
    while len(noun) < 2:
        noun = input('Type a  noun: ').strip()   
    while len(adjective) < 2:
        adjective = input('Type an adjective (feeling) : ').strip() 
    while len(verb) < 2:
        verb = input('Type a verb: ').strip()        
    while len(adjective2) < 2:
       adjective2 = input('Type an adjective (feeling): ').strip()
    while len(animal) < 2:
        animal = input('Type an animal: ').strip()     
    while len(verb2) < 2:
        verb2 = input('Type a verb: ').strip()
    while len(color) < 2:
        color = input('Type a color: ').strip()        
    while len(verb3) < 2:
        verb3 = input('Type a verb: ').strip()       
    while len(adverb) < 2:
        adverb = input('Type an adverb: ').strip() 
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
    while len(noun2) < 2:
        noun2 = input('Type a noun: ').strip()      

                  
    first_madlib = f'''This weekend I am going camping with {proper_noun}.I packed my lantern, sleeping bag, and {noun}.
        I am so {adjective} to {verb} in a tent. I am {adjective2} we might see a {animal}, they are kind of 
        dangerous. We are going to hike, fish, and {verb2}. I have heard that the {color} lake is great for
        {verb3}. Then we will {adverb} hike through the forest for {number} {measure_of_time}. If I see a 
        {color2} {animal2} while hiking, I am going to bring it home as a pet!  At night we will tell {number2}{silly_word} 
        stories and roast {noun2} around the fire'''

madlib()
print(first_madlib)    


def madlib_2():
    """ Asks the user for input, validates the input and returns the string"""
    # User input variables
    number = ""
    measure_of_time = ""
    transportation_mode = ""
    adjective1 = ""
    adjective2 = ""
    noun1 = ""
    color = ""
    part_of_body = ""
    verb = ""
    number2 = ""
    noun2 = ""
    noun3 = ""
    part_of_body2 = ""
    verb2 = ""
    noun4 = ""
    adjective3 = ""
    silly_word = ""
    noun5 = ""

    # Checking user input
    while len(number) < 2:
        num = input('Type a number: ').strip()
    while len(measure_of_time) < 2:
        measure_of_time = input('Type a measure of time: ').strip()    
    while len(transportation_mode) < 2:
        transportation_mode = input('Type a mode of transport: ').strip()  
    while len(adjective1) < 2:
        adjective1 = input('Type an adjective: ').strip()      
    while len(adjective2) < 2:
        adjective2 = input('Type an adjective: ').strip()  
    while len(noun1) < 2:
        noun1 = input('Type a noun: ').strip()
    while len(color) < 2:
        color = input('Type a color: ').strip()   
    while len(part_of_body) < 2:
        part_of_body = input('Type a body part: ').strip()     
    while len(verb) < 2:
        verb = input('Type an verb: ').strip()
    while len(number2) < 2:
        number2 = input('Type a number: ').strip()
    while len(noun2) < 2:
        noun2 = input('Type a noun: ').strip()
    while len(noun3) < 2:
        noun3 = input('Type a noun: ').strip()
    while len(part_of_body2) < 2:
        part_of_body2 = input('Type a body part: ').strip()
    while len(verb2) < 2:
        verb2 = input('Type a verb: ').strip() 
    while len(noun4) < 2:
        noun4 = input('Type a noun: ').strip()  
    while len(adjective3) < 2:
        adjective3 = input('Type an adjective: ').strip()     
    while len(silly_word) < 2:
        silly_word = input('Type a silly_word: ').strip()
    while len(noun5) < 2:
        noun5 = input('Type a noun4: ').strip()    

    second_madlib = f'''It was about {number} {measure_of_time} ago when I came to the hospital in a {transportation_mode}. The hospital is a {adjective1}
    place, there are a lot of {adjective2} {noun1} here. There are nurses here who have {color} {part_of_body}. If someone wants to come
    into my room I told them that they have to {verb} first.I have decorated my room with {number2} {noun2}. Today a 
    doctor came into my room and they were wearing a {noun3} on their {part_of_body2}. I heard that all doctors {verb2} {noun4} 
    everyday for breakfast. The most {adjective3} thing about being in the hospital is the {silly_word} {noun5}.'

   










