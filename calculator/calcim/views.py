from django.shortcuts import render

def home(request):
    result = None
    error = None

    if request.method == 'POST':
        try:
            a = float(request.POST.get("Num1"))
            b = float(request.POST.get("Num2"))
            op = request.POST.get("op").lower().strip()

            if op == "addition" or op == "add" or op == "+":
                result = a + b
            elif op == "subtraction" or op == "subtract" or op == "-":
                result = a - b
            elif op == "multiplication" or op == "multiply" or op == "*":
                result = a * b
            elif op == "division" or op == "divide" or op == "/":
                if b != 0:
                    result = a / b
                else:
                    error = "Division by zero is not allowed!"
            else:
                error = "Invalid operation!"
        except ValueError:
            error = "Please enter valid numbers."

    return render(request, 'home.html', {'result': result, 'error': error})
