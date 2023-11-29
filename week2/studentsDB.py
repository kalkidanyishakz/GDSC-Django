
students_list=[]
'''
more functionality
def validated_option_input()
def validated_property_input()
def validated_age_input()
def validated_grade_input()
def validated_section_input()--done
def validated_id_input()----done
'''
def validated_name_input(prompt):
    name=input(prompt)
    if name.strip() =="":
        print('\t...name can\'t be empty...')
        return validated_name_input(prompt)
    if len(name)<4:
        print('\t...name is too short...')
        return validated_name_input(prompt)

    if len(name)>15:
        print('\t...name is too long...')
        return validated_name_input(prompt)

    return name

def validated_grade_input(prompt):
    grades=['A','B','C','D','F']
    grade=input(prompt)
    grade=grade.upper()

    if grade in grades:
        return grade 
    else:
        print("...please enter the right grade...")
        return validated_grade_input(prompt)

def validated_section_input(prompt):
    grades=['A','B','C','D','F']
    grade=input(prompt)
    grade=grade.upper()

    if grade in grades:
        return grade 
    else:
        print("...please enter the right sectionf...")
        return validated_grade_input(prompt)


def print_student(student_object):
    def closing_bar(prop):
        spaces=27-len(str(student_object[prop]))
        bar=" "*spaces+'|'
        return bar

    print(f'''
    ------------------------------------------
    | name     | {student_object['name']} {closing_bar('name')}
    ------------------------------------------
    | age      | {student_object['age']} {closing_bar('age')}
    ------------------------------------------
    | grade    | {student_object['grade']} {closing_bar('grade')}
    ------------------------------------------
    | section  | {student_object['section']} {closing_bar('section')}
    ------------------------------------------
    | id       | {student_object['id']} {closing_bar('id')}
    ------------------------------------------
    ''')

def add_student(name, age, grade, section, id):
    student_object={
        'name':name, 
        'age':age,
        'grade':grade,
        'section':section,
        'id':id
    }
    students_list.append(student_object)
    print('A NEW STUDENT HAS BEEN ADDED\n')

def display_students():
    print('DISPLAYING ALL STUDENTS')
    for student in students_list:
        print_student(student)
    

def display_student_by_name(name):
    for student in students_list:
        if student['name']==name:
            print(f'\nDISPLAYING STUDENT BY NAME --- NAME: {name.upper()}')
            print_student(student)


        
def update_student(name, property, value):
    prev=''
    current=''
    for student in students_list:
        if student['name']==name:
            prev=str(student[property])
            student[property]=value
            current=str(student[property])

    print(f'{property.upper()} CHANGED: {prev.upper()} -> {current.upper()}')
        
        
    

#here
def delete_student(name):
    count=0
    for student in students_list:
        if student['name']==name:
            del students_list[count]
        count=count+1
            


add_student('kalkidan', 21,7, 'c', 'ETS0888/14')
add_student('surafel', 20,7, 'c', 'ETS0889/14')
update_student('surafel', 'age', 23)

def add_student_ui():
    print('\033c')
    print('ADDING A NEWE USER')
    print('.................................')
    name=validated_name_input('\tENTER THE NAME OF THE STUDENT: ')
    age=input('\tENTER AGE: ')
    grade=validated_grade_input('\tENTER GRADE: ')
    section=input('\tENTER SECTION: ')
    id=input('\tENTER ID: ')
    print('.................................')
    add_student(name, age, grade, section, id)

def display_student_by_name_ui():
    print('\033c')
    print('DISPLAY STUDENT')
    print('.................................')
    name=validated_name_input('\tENTER NAME: ')
    print('.................................')
    display_student_by_name(name)


def update_student_by_name_ui():
    print('\033c')
    print('UPDATE STUDENT INFORMATION')
    print('.................................')
    name=validated_name_input('\tENTER NAME: ')

    my_value=int(input('''
        CHOOSE A PROPERTY YOU WANT TO UPDATE
        ......................
        [1] NAME  
        [2] AGE  
        [3] GRADE  
        [4] SECTION  
        [5] ID
        ......................

        ENTER A NUMBER: '''))

    my_list=['name', 'age', 'grade', 'section', 'id']
    prop=my_list[my_value-1]

    val=input(f'\n\tENTER A VALUE FOR {prop.upper()}: ')
    print('.................................')
    
    update_student(name, prop, val)



def display_students_ui():
    print('\033c')
    display_students()


def delete_student_by_name_ui():
    print('\033c')
    print('DELETE STUDENT')
    print('.................................')
    name=validated_name_input('\tENTER NAME: ')
    print('.................................')
    print(f'STUDENT {name.upper()} HAS BEEN DELETED')
    delete_student(name)



def display_options():
    val=input("\nENTER ANY KEY TO CONTINUE: ")
    print('\033c')
    my_value=input('''
    ......................................
    [1] ADD STUDENT
    [2] DISPLAY STUDENT
    [3] LIST ALL STUDENTS
    [4] UPDATE STUDENT INFORMATION
    [5] DELETE STUDENT
    [6] EXIT
    ......................................

    ENTER A NUMBER: ''')
    my_value=int(my_value)
    
    match my_value:
        case 1:
            add_student_ui()
            display_options()
        case 2:
            display_student_by_name_ui()
            display_options()
        case 3:
            display_students_ui()
            display_options()
        case 4:
            update_student_by_name_ui()
            display_options()
        case 5:
            delete_student_by_name_ui()
            display_options()
        case 6:
            print('\033c')
            print('THANK YOU')


display_options()

