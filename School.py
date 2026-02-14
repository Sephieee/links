school = ''
enroll = ''

while True:
    print('\nWelcome to the schoolet')

    school = input("""
Continue type 'yes'
""")

    if school == 'yes':
        print('\nYes')
        print('No')
        school = input('\nAre you a student of my schoolet? ')
        
        if school == 'yes':

            school_id = int(input('Input your school id number'))

        elif school == 'no':
            print('Do want to enroll in schoolet? ')
            
            
        