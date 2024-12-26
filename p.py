from datetime import datetime
import unittest
import os


def s_write(data):
    f_path = "profile.txt"
    with open(f_path,"a")as file:
        file.write(data + "---")
        
        
        

def student():
    while True:
        try:
            f_name = open("profile.txt","a")
            s_first = input("enter your first name: ")
            s_first = s_first.strip()
            if s_first.isalpha():
                
                s_write(s_first)
                break
            else:
                print("first name has some error")
                continue
        except ValueError:
            print(ValueError)
    while True:
        try:
            f_name = open("profile.txt","a")
            s_last = input("enter your last name: ")
            s_last = s_last.strip()
            if s_last.isalpha():
                
                s_write(s_last)
                break
            else:
                print("last name has some error")
                continue
        except ValueError:
            print(ValueError)
    
def dob():
    while True:
        f_name = open("profile.txt","a")
        s_dob = input("Enter your date of birth (MM/DD/YYYY):")
        try:
            datetime.strptime(s_dob, "%m/%d/%Y")
            s_write(s_dob)
            break
        except ValueError:
            print("Error: incorrect date format. Please use MM/DD/YYYY")
            continue
    return (s_dob)
def gender():
    while True:
        f_name = open("profile.txt","a")
        s_gender = input("Enter your gender(M/F):").upper()
        if s_gender in ["M","F"]:
            s_write(s_gender)
            break
        else:
            print("there is a issue your gender")
            continue
        return (s_gender)
def age():
    while True:
        try:
            f_name = open("profile.txt","a")
            
            s_age = int(input("Enter how old you are"))
            if s_age > 100 or s_age < 0:
                        
                        print("how can you be",s_age,"lol")
                        continue
            else:
                s_age = str(s_age)
                s_write(s_age)
                break
        except ValueError:
            print("There has been a age error please ensure it is correct")

    return(s_age)
def course():
    while True:
        f_name = open("profile.txt","a")
        try:
            s_course = input("Enter the course").upper()
            if s_course in ["CS","IS"]:
                s_write(s_course)
                break
            else:
                print("your course has not been there only CS and IS")
                continue
        except ValueError:
            print("something didnt go as planned")

    return(s_course)

        
def backup(source = "profile.txt"):
    try:
        f = open("profile.txt")
        f.close()
    except FileNotFoundError:
        print("File does not exist")
    
    target = "copied"+source
    data = []
    with open(source,"r") as fr:
        for line in fr:
            line = line.strip()
            data.append(line)
    with open(target, "w") as fw:
        for i in range(len(data)):
            line = str(i+1) + "." + data[i]
            fw.write(line)
            fw.write("\n")
def create_profiles():
    data = []
    while True:
        main()
        data.append(main)
        c = input('Continue ... (Y/N) ')
        if c.upper() == 'N':
            
            break
    return data



def main():
    student()
    dob()
    age()
    gender()
    course()
    backup()
    
create_profiles()

    
