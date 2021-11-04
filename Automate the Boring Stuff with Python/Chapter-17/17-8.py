import subprocess
import os

print("Launching Other Programs from Python")
calculator = subprocess.Popen("c:\\Windows\\System32\\mspaint.exe")
print(calculator.poll())  # revisa si el programa fue cerrado
# suspende la ejecucion hasta que el progrma sea cerrado
# ciertos progmas (como la calculadora) no sirven con wait()
print(calculator.wait())
print(calculator.poll())
