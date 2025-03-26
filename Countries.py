class Sri_Lanka():
    def capital(self):
        print("Sri Lanka's capital is Sri Jayawardhna Pura Kootte")
    def language(self):
        print("Sinhala is the most widely spoken language in Sri Lanka")
    def type(self):
        print("Sri Lanka is a developing country")

class USA():
    def capital(self):
        print("USA's capital is Washington,DC")
    def language(self):
        print("English is the most widely spoken language in Sri Lanka")
    def type(self):
        print("USA is a developed country")

obj_srlk=Sri_Lanka()
obj_usa=USA()

for country in (obj_srlk,obj_usa):
    country.capital()
    country.language()
    country.type()

