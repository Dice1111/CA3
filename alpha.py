from tabulate import tabulate
import datetime



# Dictionary Variables.............


swimmers = {'Mgmg': {'Name': ['Mgmg'], 'Age': ['18'], 'Gender': ['male'] ,'Status' : ['active'],'Event':[None],'Time':[None],"Meet":[None]}}



record_swimmers_temp ={'Mgmg': {'Name': ['Mgmg'], 'Age': ['18'], 'Gender': ['male'] ,'Status' : ['active'],'Event':[],'Time':[],"Meet":[],'Post_Status':'Unposted'}}


record_swimmer_real = {'Mgmg': {'Name': ['Mgmg'], 'Age': ['18'], 'Gender': ['male'] ,'Status' : ['active'],'Event':[],'Time':[],"Meet":[],'Post_Status':'posted'}}

record_swimmer_real_table= {'Name':[],"Age":[],"Gender":[],"Status":[],"Event":[],"Time":[],"Meet":[]}


#register_status
reg_status_true = "active"
reg_status_false = "inactive"

#post status
post_status_true ="posted"
post_status_false ="unposted"

# function
#input_validation_function
def check_name(check_reg_name):
    
    if check_reg_name.isalpha():
        return True
    else:
        return False

#check date function
def check_date(check_reg_date):

    year,month,day = check_reg_date.split('/')
    #check input_validation_for age
    
    try:
        datetime.datetime(int(year),int(month),int(day))
    except ValueError:
        return False

#check gender

def check_gender(check_reg_gender):
    
    if check_reg_gender == '1':
        return ['Male']
    elif check_reg_gender == '2':
        return ['Female']
    elif check_reg_gender == '3':
        return ['Others']
    else:
        return False


#Main Program.........

#For Registering.....................

main_program = True
while main_program == True:
    user_choice = input("\n\n\nFor register press 1\nFor record swimmer time press 2\nFor search individual press 3\nTo display unposted press 4\nTo execute program press 5\nEnter Your option:")
    if user_choice == '5':
        main_program = False
    if user_choice == '1':

        input_loop = True
    
        while input_loop == True:

            reg_name  = input("Enter name:")

            #check input_validation_for name  
            check_name(reg_name)                                 
            while check_name(reg_name) == False:
                print("Only allow alphabets for name")
                reg_name  = input("Enter name:")
                check_name(reg_name)



            if reg_name in swimmers and [reg_status_false] == swimmers[reg_name]['Status']:
                swimmers[reg_name]['Status'] = [reg_status_true]
                print("This username is now active")
                input_loop = True

            elif reg_name in swimmers and [reg_status_true] == swimmers[reg_name]['Status']:
                print("This user is already active")
                input_loop = True
            else:
                input_loop = False
                swimmers[reg_name]={}
                swimmers[reg_name]['Name']=[reg_name]

                reg_dob= input("Enter data of birth in format yy/mm/dd:")

                #check input_validation_for dateTime  
                check_date(reg_dob)
                while check_date(reg_dob) == False:
                    print("Input date is not valid..")
                    reg_dob= input("Enter data of birth in format yy/mm/dd:")
                    check_date(reg_dob)
                swimmers[reg_name]['Age']=[reg_dob] 


                reg_gen= input("Enter 1 for Male\nEnter 2 for Female\nEnter 3 for Others\nEnter your gender number:")
                check_gender(reg_gen)
                while check_gender(reg_gen) == False:
                    reg_gen= input("Enter 1 for Male\nEnter 2 for Female\nEnter 3 for Others\nEnter your gender number:")
                    check_gender(reg_gen)
                    
                swimmers[reg_name]['Gender']=check_gender(reg_gen)

            
                swimmers[reg_name]['Status']=[reg_status_true]
                swimmers[reg_name]['Event']=[None]
                swimmers[reg_name]['Time']=[None]
                swimmers[reg_name]['Meet']=[None]


                print("Register Successful and now active")
                print(swimmers)
                # main_program = True
        register_swimmers_table={'Name':[],"Age":[],"Gender":[],"Status":[],"Event":[],"Time":[],"Meet":[]}
        for x in swimmers.values():
        
            for a in x['Name']:
                register_swimmers_table['Name'].append(a)

            for a in x['Age']:
                register_swimmers_table['Age'].append(a)

            for a in x['Gender']:
                register_swimmers_table['Gender'].append(a)

            for a in x['Status']:
                register_swimmers_table['Status'].append(a)

            for a in x['Event']:
                register_swimmers_table['Event'].append(a)
                    
            for a in x['Time']:
                register_swimmers_table['Time'].append(a)
                    
            for a in x['Meet']:
                register_swimmers_table['Meet'].append(a)
                

        print(tabulate(register_swimmers_table, headers='keys'))            
        main_program = True


#...........................Record Swimmers..........................
    elif user_choice == '2':
        record_name = input('Enter player name to record(must be registered):')

        if record_name in swimmers:

            record_event_type =input("Choose the event type\nPress 1 for Freestyle\nPress 2 for Backstroke\nPress 3 for Breaststroke\nPress 4 for Butterfly\nPress 5 for individual Medley\nEnter your type:")

            if record_event_type == '1':
                record_event_type_detail = "Freestyle"
                record_event_meter= input('Choose between meter 50,100,200,400,800,1500:')
            elif record_event_type == '2':
                record_event_type_detail = "Backstroke"
                record_event_meter= input('Choose between meter 50,100,200:')
            elif record_event_type == '3':
                record_event_type_detail = "Breaststroke"
                record_event_meter= input('Choose between meter 50,100,200:')
            elif record_event_type == '4':
                record_event_type_detail = "Butterfly"
                record_event_meter= input('Choose between meter 50,100,200:')
            elif record_event_type == '5':
                record_event_type_detail = "individual Medley"
                record_event_meter= input('Choose between meter 100,200,400:')
            else:
                print("invaild input")
                main_program = True

            record_time=input("Enter time to record(eg.01:11:00):")
            record_meet=input("Enter the name of competition:")


            # if record_event_type_detail in record_swimmer_real[record_name]['Event'] and record_time in record_swimmer_real[record_name]['Time'] and record_meet in record_swimmer_real[record_name]['Meet']:
            #         print("You can not add same record twice")
            #         main_program = True

            if 1 == 1:

    #......................................Check Already Record and Register swimmer............................            
                if record_name in list(swimmers.keys()) and record_name in list(record_swimmer_real.keys()):
                    record_swimmers_temp[record_name]['Name'].append(record_swimmer_real[record_name]['Name'][0])
                    record_swimmers_temp[record_name]['Age'].append(record_swimmer_real[record_name]['Age'][0])
                    record_swimmers_temp[record_name]['Gender'].append(record_swimmer_real[record_name]['Gender'][0])
                    record_swimmers_temp[record_name]['Status'].append(record_swimmer_real[record_name]['Status'][0])
                    record_swimmers_temp[record_name]['Event'].append(record_event_type_detail)
                    record_swimmers_temp[record_name]['Time'].append(record_time)
                    record_swimmers_temp[record_name]['Meet'].append(record_meet)
                    record_swimmers_temp[record_name]['Post_Status'].append([post_status_false])
                
    #......................................Check Register swimmer but not Record............................  
                elif record_name in list(swimmers.keys()) and record_name not in list(record_swimmer_real.keys()):
                    #  swimmers[record_name]['Event'].append(record_event_type_detail)
                    #  swimmers[record_name]['Time'].append(record_time)
                    #  swimmers[record_name]['Meet'].append(record_meet)
                    record_swimmers_temp[record_name]={}
                    record_swimmers_temp[record_name]['Name']=[record_name]
                    record_swimmers_temp[record_name]['Age']=[swimmers[record_name]['Age']]
                    record_swimmers_temp[record_name]['Gender']=[swimmers[record_name]['Gender']]
                    record_swimmers_temp[record_name]['Status']=[swimmers[record_name]['Status']]
                    record_swimmers_temp[record_name]['Event'].append(record_event_type_detail)
                    record_swimmers_temp[record_name]['Time'].append(record_time)
                    record_swimmers_temp[record_name]['Meet'].append(record_meet)
                    record_swimmers_temp[record_name]['Post_Status']=[post_status_false]

                record_swimmers_temp_table ={'Name':[],"Age":[],"Gender":[],"Status":[],"Event":[],"Time":[],"Meet":[],'Post_Status':[]}

                for x in record_swimmers_temp.values():

                    for a in x['Name']:
                        record_swimmers_temp['Name'].append(a)

                    for a in x['Age']:
                        record_swimmers_temp['Age'].append(a)

                    for a in x['Gender']:
                        record_swimmers_temp['Gender'].append(a)

                    for a in x['Status']:
                        record_swimmers_temp['Status'].append(a)

                    for a in x['Event']:
                        record_swimmers_temp['Event'].append(a)
                    
                    for a in x['Time']:
                        record_swimmers_temp['Time'].append(a)
                    
                    for a in x['Meet']:
                        record_swimmers_temp['Meet'].append(a)
                        
                    for a in x['Post_Status']:
                        record_swimmers_temp['Post_Status'].append(a)
                

                print(tabulate(record_swimmers_temp_table, headers='keys'))            
                main_program = True
                

        else:
            print("no user found")
            main_program = True
    


