class tools:

    def __init__(self, lista:list):
        self.self = self
        self.lista = lista


    def prime(self, a):
        return a % 2 !=0


    def list_comprobation(self):
        for element in self.lista:
            if element %  2 == 0:
                print(f"{element} It´s not a prime number")
            else:
                print(f"{element} Its a prime number")




    def celsious_conversor(self):
        menu = """
            Write the option that you want to do

            Celsious to farenheit  --- 1
              Celsius to Kelvin    --- 2
              Kelvin to farenheit  --- 3
             Fahrenheit to kelvin  --- 4
                     
                     Exit          --- 5
        """

        while True:
            print(menu)
            answer = int(input("Put the option:   "))

            if answer == 4:
                return "Thanks"

            if answer == 1:

                celsius = float(input("You can write a celsius value less with ',':   "))


                fahrenheit = (celsius * 9/5 ) + 32
                print("")
                print("F° = ", fahrenheit)
                print("")

            elif answer == 2:

                celsius = float(input("You can write a celsius value less with ',':   "))

                kelvin = celsius + 273.15
                print("")
                print("K° = ", kelvin)
                print("")

            elif answer == 3:

                kelvin = float(input("Input a value to transform to farenheit:   "))

                fahrenheit = (kelvin - 273.15) * 9/5 +32

                print("")
                print("F° = ", fahrenheit)
                print("")

            elif answer == 4:

                fahrenheit= float(input("Input a value to transform to farenheit:   "))

                kelvin = (fahrenheit - 32) * 5/9 + 255.372

                print("")
                print("F° = ", fahrenheit)
                print("")





    def factorial(self):
        for i in self.lista:
            print('El factorial de ', i, 'es', self.__factorial(i))


    def __factorial(self, var):
        
        if (type(var) != int):
            print("You must write a integer")
            var = int(var)
            if var < 0:
                print("Factorial of numbers lessers than 0 aren´t exists.")
            else:
                self.__factorial(var)
        if var == 0:
            return 1

        else:
            return var * self.__factorial(var-1)

        if(type(var) != int):
            return 'El numero debe ser un entero'
        if(var < 0):
            return 'El numero debe ser pisitivo'
        if (var > 1):
            var = var * self.__factorial(var - 1)
        return var



    def counter(self, my_list : list):

        while True:

            print("What do you want to do?")

            print("")

            print("Print min value  ---  press '1'")

            print("Print max value  ---  press '2'")

            print("      Exit       ---  press '3'")


            print("")

            answer = int(input("Write your answer here!:     "))

            if answer == 3:
                print( "Thanks")
                return


            dict={}
            
            dict = { element : my_list.count(element) for element in my_list}
            
            print(dict)

            if answer == 1:
                min_key = min(dict, key=lambda key: dict[key])
                if dict[min_key] > 1:
                    print(f"The key with lesser value is: {min_key} with {dict[min_key]} times repeated")
                else:
                    print(f"The key with lesser value is: {min_key} with {dict[min_key]} time repeated")


            else:
                max_key = max(dict, key=lambda key: dict[key])
                print(f"The key with bigger value is: {max_key} with {dict[max_key]} times repeated")
