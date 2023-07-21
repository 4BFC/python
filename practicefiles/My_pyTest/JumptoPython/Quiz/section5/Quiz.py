class Family:
    lastname = "김"


a = Family()
b = Family()

Family.lastname = "박"
print(a.lastname)
print(b.lastname)
