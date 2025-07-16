import re

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "❌ Error! Division by zero."
        return x / y

    def safe_eval(self, expression: str):
        # Allow only numbers, operators, parentheses, and spaces
        if not re.fullmatch(r'[\d\s\+\-\*\/\(\)]+', expression):
            return "❌ Invalid characters detected. Use only numbers and + - * / ( ) symbols."

        try:
            # Evaluate the arithmetic expression safely
            # Note: eval here only works because of the regex filter above
            result = eval(expression)
            # Check division by zero if result is infinity or error occurs (handled by exception)
            if result == float('inf') or result == float('-inf'):
                return "❌ Error! Division by zero."
            return result
        except ZeroDivisionError:
            return "❌ Error! Division by zero."
        except Exception as e:
            return f"❌ Error: Invalid expression ({str(e)})"


print("📟 Calculator App | Supports +, -, *, / and parentheses ()")
print("🔁 Type expressions like: (4+5)*8 or 5*(2+3)or 4+5, 6+7*8")
print("❌ Type 'exit' to quit\n")

calc = Calculator()

while True:
    user_input = input("> ").strip()

    if user_input.lower() in ['exit', 'quit', 'stop']:
        print("👋 Exiting. Bye!")
        break

    if re.search(r'[^0-9+\-*/().\s]', user_input):
        print("❌ Use only numbers and + - * / ( ) symbols.")
        continue

    result = calc.safe_eval(user_input)
    print("✅ Result:", result)
