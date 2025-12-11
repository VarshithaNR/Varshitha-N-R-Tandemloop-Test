class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def compute(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "subtract":
            return self.a - self.b
        elif self.operation == "multiply":
            return self.a * self.b
        elif self.operation == "divide":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"
        else:
            return "Invalid Operation"


# Example
a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
operation = input("Enter operation (add, subtract, multiply, divide): ")

calc = Calculator(a, b, operation)
print("Result:", calc.compute())
