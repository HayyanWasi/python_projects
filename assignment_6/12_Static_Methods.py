class TemperatureConverter:
    @staticmethod
    def celcius_to_farenheit(c):
        F = (9/5*c)+32
        return F
    


temp_input = float(input("Enter temp in celcius\n"))
celsius_to_farenheit = TemperatureConverter.celcius_to_farenheit(temp_input)
print(f"{celsius_to_farenheit} farenheit")
    

