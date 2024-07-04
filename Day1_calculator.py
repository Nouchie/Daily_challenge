class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y
    
    def subtract(self):
        return self.x - self.y
    
    def divide(self):
        if self.y == 0:
            return "Cannot divide by zero!"
        return self.x / self.y
    
    def multiply(self):
        return self.x * self.y

def main():
    while True:
        x_input = input("Give an X value or Q to quit: ").strip().lower()
        if x_input == 'q':
            break
        
        y_input = input("Give a Y value or Q to quit: ").strip().lower()
        if y_input == 'q':
            break
        
        try:
            x = int(x_input)
            y = int(y_input)
            operation = Calculator(x, y)
            quest = input("What do you want to do? (add, subtract, divide, multiply) ").strip().lower()
            if quest == 'add':
                print(operation.add())
            elif quest == 'subtract':
                print(operation.subtract())
            elif quest == 'divide':
                print(operation.divide())
            elif quest == 'multiply':
                print(operation.multiply())
            else:
                print("Give a correct operation.")      
        except ValueError:
            print("Give an integer for X and Y.")

if __name__ == "__main__":
    main()
