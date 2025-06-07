
unit_cm = "centimetre"
unit_pouce = "inches"
nb_valeus = 2.54

def unit_request():
    nb_int = 0
    while nb_int == 0: 

        unit_choise = input(f"Want to convert from \"{unit_pouce} to {unit_cm}\" select 1 or \"{unit_cm} to {unit_pouce}\" select 2 ? ")

        try:
            nb_int = int(unit_choise)
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
        else:
            if nb_int < 1 or nb_int > 2: 
                print(f"Oops! Error please read the question carefully !! Try again...")
                nb_int = 0

    return nb_int

def conversion(unit):

    nb_conversion = 0.0
    nb = ""
    select_unit = ""
    unit_convert = ""

    while nb_conversion == 0.0: 

        if unit == 1:
          select_unit = unit_pouce
          unit_convert = unit_cm
          nb = input(f"Please enter the number in {unit_pouce} you wanted to convert?") 

          try:
            nb_1 = float(nb) 
            nb_conversion = nb_1 * nb_valeus
          except ValueError:
            print("Oops!  That was no valid number.  Try again...")
          
        elif unit == 2:
          select_unit = unit_cm
          unit_convert = unit_pouce
          nb = input(f"Please enter the number in {unit_cm} you wanted to convert?") 

          try:
            nb_2 = float(nb) 
            nb_conversion = nb_2 / nb_valeus
          except ValueError:
            print("Oops!  That was no valid number.  Try again...")

        else:
           print("Oops! Error in the program Please contact support ...")

    return nb_conversion , nb , select_unit , unit_convert

result = unit_request()
retults_conveter , value , unit1 , unit2 = conversion(result)
print(f"The valeus {value} {unit1} is equal to {retults_conveter} of an {unit2}")
