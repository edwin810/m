

import datetime
from datetime import datetime


class Student:
    def __init__(self,
                 uid,
                 first_name,
                 middle_name,
                 last_name,
                 gender,
                 dob,
                 email,
                 bio
                    ):
        
        if uid.strip() == "":
            raise ValueError("ID is empty")
        self.uid = uid

        if first_name.strip() == "":
            raise ValueError("First name is empty")
        self.first_name = first_name

        if middle_name.strip() == "":
            raise ValueError("Middle name is empty")
        self.middle_name  = middle_name

        if last_name.strip() == "":
            raise ValueError("Last name is empty")
        self.last_name = last_name

        if gender.strip() not in ["M","F","Male","Female"]:
            raise ValueError("Gender is invalid " + str(gender) )
        self.gender = gender


        if dob.strip() == datetime.fromisoformat(dob):
            raise ValueError("Date of birth is empty")
            try:
                self.dob = datetime.fromisoformat(dob)
            except:
                raise ValueError("Invalid Date of Birth: " + dob)
            
            raise ValueError("ID is empty")
        
        self.dob = dob

        if email.strip() == "":
            raise ValueError("Email is empty")
        self.email = email

        if bio.strip() == "":
            raise ValueError("bio is No provided")
        self.bio = bio
        
    def get_full_name(self):
        
        return(self.first_name,self.middle_name,self.last_name)
    
    def get_info(self):
        return (self.uid,self.first_name,self.middle_name,self.last_name,self.gender,
                self.gender,self.dob,self.email,self.bio)
    
    def update_bio(self,bio = "Not provided"):
        self.bio = bio

    def update_email(self,email):
        self.email = email 
        
    def _str_(self):
        info = self.uid + ":" + self.first_name + ":" + self.middle_name + ":" + self.last_name + ":" + self.gender + ":" + self.dob + ":" + self.email + ":" + self.bio + ":"
        return info

    def display_info(self):
        
        msg = """
                UID = {uid}
                First name: = {first_name}
                Second name = {middle_name}
                Last name  = {last_name}
                Gender = {gender}
                Birthday : {dob}
                Email : {email}
                Bio : {bio}
            """
        info = msg.format(
            uid = self.uid,
            first_name = self.first_name,
            middle_name = self.middle_name,
            last_name = self.last_name,
            gender  = self.gender,
            dob = self.dob,
            email = self.email,
            bio = self.bio)
        print (info)

        
    
        



