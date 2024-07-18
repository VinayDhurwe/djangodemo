from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'text_tools/index.html')

def reverse_string(request):
    if request.method == 'POST':
        input_text = request.POST['input_text']
        reversed_text = input_text[::-1]
        return render(request, 'text_tools/reverse.html', {'result': reversed_text})
    return render(request, 'text_tools/reverse.html')

def fibonacci(request):
    if request.method == 'POST':
        number = int(request.POST['number'])
        fib_sequence = [0, 1]
        while len(fib_sequence) < number:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return render(request, 'text_tools/fibonacci.html', {'result': fib_sequence[:number]})
    return render(request, 'text_tools/fibonacci.html')

def palindrome(request):
    result = None  # Initialize result variable
    
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')  # Use .get() to avoid KeyError
        is_palindrome = input_text == input_text[::-1]
        result = f"'{input_text}' is a palindrome." if is_palindrome else f"'{input_text}' is not a palindrome."
    
    return render(request, 'text_tools/palindrome.html', {'result': result})