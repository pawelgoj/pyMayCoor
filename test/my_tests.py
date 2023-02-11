
import subprocess


fn = 'test/tmp/data0/out.txt'
print(fn)
subprocess.run(f'python3_10 main/main.py -i ./egzamples_instructions/out1.txt -s ./egzamples_instructions/settings.yaml -o {fn}', shell=True)

# os.system(f'python3_10 main/main.py -i ../egzamples_instructions/out1.txt -s ../egzamples_instructions/settings.yaml -o {fn}')
with open(str(fn), 'r', encoding="utf-8") as file:
    print(file.read())
assert True
