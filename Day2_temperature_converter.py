
class Temperature:
    def __init__(self, kelvin=0, celsius=0, fahren=0):
        self.kelvin = kelvin
        self.celsius = celsius
        self.fahren = fahren

    def celsius_to_kelvin(self):
        kelvin = self.celsius + 273.15
        return kelvin
    
    def kelvin_to_celsius(self):
        celsius = self.kelvin - 273.15
        return celsius
    
    def fahren_to_celsius(self):
        celsius = (self.fahren - 32) * (5 / 9)
        return celsius
    
    def celsius_to_fahren(self):
        fahren = self.celsius * (9 / 5) + 32
        return fahren
    
    def fahren_to_kelvin(self):
        kelvin = (self.fahren - 32) * (5 / 9) + 273.15
        return kelvin
    
    def kelvin_to_fahren(self):
        fahren = (self.kelvin - 273.15) * (9 / 5) + 32
        return fahren
    
def main():
    while True:
        convert1 = input("What conversion do you want to do? (fahren/celsius/kelvin/q to Quit) ").strip().lower()
        if convert1 == "q":
            break

        convert2 = input("What do you want it to? (fahren/celsius/kelvin/q to Quit) ").strip().lower()
        if convert2 == "q":
            break
        
        # Fahrenheit to Celsius
        if convert1 == "fahren" and convert2 == "celsius":
            fahren_input = input("Enter Fahrenheit value: ")
            try:
                fahren = float(fahren_input)
                temp = Temperature(fahren=fahren)
                print(temp.fahren_to_celsius())
            except ValueError:
                print("Give a valid number for Fahrenheit")

        # Kelvin to Celsius
        elif convert1 == "kelvin" and convert2 == "celsius":
            kelvin_input = input("Enter Kelvin value: ")
            try:
                kelvin = float(kelvin_input)
                temp = Temperature(kelvin=kelvin)
                print(temp.kelvin_to_celsius())
            except ValueError:
                print("Give a valid number for Kelvin")

        # Celsius to Fahrenheit
        elif convert1 == "celsius" and convert2 == "fahren":
            celsius_input = input("Enter Celsius value: ")
            try:
                celsius = float(celsius_input)
                temp = Temperature(celsius=celsius)
                print(temp.celsius_to_fahren())
            except ValueError:
                print("Give a valid number for Celsius")

        # Kelvin to Fahrenheit
        elif convert1 == "kelvin" and convert2 == "fahren":
            kelvin_input = input("Enter Kelvin value: ")
            try:
                kelvin = float(kelvin_input)
                temp = Temperature(kelvin=kelvin)
                print(temp.kelvin_to_fahren())
            except ValueError:
                print("Give a valid number for Kelvin")

        # Fahrenheit to Kelvin
        elif convert1 == "fahren" and convert2 == "kelvin":
            fahren_input = input("Enter Fahrenheit value: ")
            try:
                fahren = float(fahren_input)
                temp = Temperature(fahren=fahren)
                print(temp.fahren_to_kelvin())
            except ValueError:
                print("Give a valid number for Fahrenheit")

        # Celsius to Kelvin
        elif convert1 == "celsius" and convert2 == "kelvin":
            celsius_input = input("Enter Celsius value: ")
            try:
                celsius = float(celsius_input)
                temp = Temperature(celsius=celsius)
                print(temp.celsius_to_kelvin())
            except ValueError:
                print("Give a valid number for Celsius")


if __name__ == "__main__":
    main()
