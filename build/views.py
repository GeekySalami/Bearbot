from django.shortcuts import render
from django.http import HttpResponse

def wrkspace(request):
       
    return render(request, 'build/workspace.html')

def execute_code(request):
    if request.method == "POST":
        editordata = request.POST['codearea']

        try:
            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')

            exec(editordata)
            sys.stdout.close()

            sys.stdout = original_stdout

            output = open('file.txt', 'r').read()

        except Exception as e:
            sys.stdout = original_stdout
            output = e
    return render(request, 'build/workspace.html', {'code':editordata}, {'output':output})