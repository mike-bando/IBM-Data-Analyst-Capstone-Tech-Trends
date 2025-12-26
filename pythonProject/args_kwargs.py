
# shipping label based on args & kwargsS

print(' ')
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print("\n")
    

    if "flat_number" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('number')}, flat no: {kwargs.get('flat_number')}")
    else:
         print(f"{kwargs.get('street')} {kwargs.get('number')}")

    print(f"{kwargs.get('city')}, {kwargs.get('voivodeship')}, {kwargs.get('country')}")

shipping_label("Mr",'Michal','Bando', 
               street="Ogrodowa",
               number = "25",
            #    flat_number = "01",
               city = "Kalwaria Zebrzydowska",
               voivodeship = "Malopolska",
               country='Polska')


