# reading code from a file
f = open('2.py', 'r')
code_str = f.read()
f.close()
code = compile(code_str, '2.py', 'exec')
exec(code)