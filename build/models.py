from django.db import models
import sys

class Code(models.Model):
    
    try:
        code = models.TextField()
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
