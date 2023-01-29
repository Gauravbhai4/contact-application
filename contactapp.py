class person:
    def __init__(self,name,last,phone,email):
        if type(phone) is str:
            phone=[phone]
        if type(email) is str:
            email=[email]
        email =[str(mail).lower() for mail in email]
        self.name=name
        self.last= last
        self.phone=phone
        self.email=email
    def __str__(self):
        phone=", ".join(self.phone)
        email =', '.join(self.email)
        return f"""
         name ={self.name} {self.last}
        phone ={phone}
        email ={email}
        """
class addperson:
    def __init__(self):
        self.contact={}
    def addcontact(self,person):
        if person.last.lower() in self.contact.keys():
            self.contact[person.last].append(person)
        else:
            self.contact[person.last]=[person]
    def show_all(self):
        for lst in self.contact.values():
            for person in lst:
                print(person)
    def lookup(self,lastname,firstname=None):
        contact=self.contact.get(lastname.lower().strip())
        if contact:
            for person in contact:
                if firstname!=None:
                    if person.name.lower()==firstname.lower():
                        print(person)
                else:
                    print(person)
