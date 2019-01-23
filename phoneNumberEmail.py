#! Python 3
#this program will allow you to enter any block of text and will tweeze out the
#phone numbers, the emails, or both depending on what you want

import pyperclip, re, os

which_thing = input("would you like me to find, email, phone numbers, or both? (P for phonenumbers, E for email, and B for both)")
     
phone_number = re.compile(r'''(
  (\d{3} | \(\d{3}\))?  #area code
  (\s|-|\.)?            #seperator
  (\d{3})               #first 3 digits
  (\s|-|\.)?            #seperator
  (\d{4})               #last 4 digits
  )''' , re.VERBOSE)

email = re.compile(r'''(
    [a-zA-z0-9._%+-]+   #usermname
    @                   #@ symbol
    [a-zA-Z0-9.-]+      #domain name
    (\.[a-zA-Z]{2,4})   #dot-something
    )''', re.VERBOSE)

text = str(pyperclip.paste())

#function for adding the matches to the clipboard
def add_to_clip(matches, matches2) :
    if len(matches) > 0 and len(matches2) > 0 :
        all_the_matches = matches + matches2
        pyperclip.copy(' '.join(all_the_matches))
        message = "both phone numbers and emails have been copied to the clipboard"
        return message
    elif len(matches) > 0 and len(matches2) == 0 :
        pyperclip.copy(' '.join(matches))
        message = "phone numbers were copied to the clipboard"
        return message
    elif len(matches) == 0 and len(matches2) > 0 :
        pyperclip.copy(' '.join(matches2))
        message = "emails were copied to the clipboard"
        return message
    else :
        message = "something has gone wrong"
        return message
    

#function for finding all the emails
def email_finder(this_text, email_regex) :
    email_matches = []
    for groups in email_regex.findall(this_text) :
        email_matches.append(groups[0])
    if len(email_matches) > 0 :
        print("I found some emails")
        return email_matches
    else :
        print("none were found")
        return email_matches
             
    

#function for finding all the phone numbers in text block
def phone_number_finder(this_text, phone_number_regex) :
    phone_number_matches = []
    for groups in phone_number_regex.findall(this_text) :
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])
        phone_number_matches.append(phoneNum)
    if len(phone_number_matches) == 0 :
        print("no phone number matches were found")
        return phone_number_matches
    else :
        print("I found some phone numbers")
        return phone_number_matches
    

if which_thing.lower() == "p" :
    
    email_place_holder = []
    returned_phone_numbers = phone_number_finder(text, phone_number)
    match_message = add_to_clip(returned_phone_numbers, email_place_holder)
    print(match_message)
    
elif which_thing.lower() == "e" :
    
    phone_number_place_holder = []
    returned_emails = email_finder(text, email)
    match_message = add_to_clip(returned_emails, phone_number_place_holder)
    print(match_message)
    
elif which_thing.lower() == "b" :
    
    returned_phone_numbers = phone_number_finder(text, phone_number)
    returned_emails = email_finder(text, email)
    match_message = add_to_clip(returned_phone_numbers, returned_emails)
    print(match_message)
    

    




    
