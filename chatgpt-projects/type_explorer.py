x = input("Enter anything: ")

try:
    x = int(x)
    print(type(x))
    x = float(x)
    print(type(x))
except ValueError:
    print("Input Cannot Be converted to float.")
    print(type(x))
    print(x)
else:
    print(x)
    