from django.shortcuts import render
import sys
from io import StringIO
from . import forms
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import subprocess


def wrkspace(request):
    return render(request, 'build/workspace.html')

@csrf_exempt  
def run_code(request):
    if request.method == 'POST':
        try:
            code = request.POST['code']
            input_data = (request.POST['input'])

            input_data = input_data.replace("\n"," ").split(" ")

            language = request.POST['language']  
        except KeyError:
            return JsonResponse({'error': 'Missing required data (code, input, language)'}, status=400)

        
        for i in input_data:
            print({code}," ", {i})

        
        #orig_stdout = None
        try:
            input_bytes = "\n".join(input_data).encode()

            
            process = subprocess.Popen(['python3', '-c', code], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            
            #output, error = process.communicate(input=input_bytes)
            process.stdin.write(input_bytes)
            process.stdin.close()
            
            output = process.stdout.read()
            output = output.decode()

        except Exception as e:
            #sys.stdout.close()
            #sys.stdout=orig_stdout
            output = str(e)
        print({output})
        return JsonResponse({'result': output})

    else:
        return render(request,'build/workspace.html')


'''
def execute_code(request):
    if request.method == 'POST':
        code_part = request.POST['codearea']
        #input_part = request.POST['input_area']
        #y = input_part
        #input_part = input_part.replace("\n"," ").split(" ")
        #def input():
        #    a = input_part[0]
        #    del input_part[0]
        #    return a
        try:
            orig_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code_part)
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = open('file.txt', 'r').read()
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
        print({output})
    return render(request,'build/workspace.html',{"code":code_part,"output":output})
'''