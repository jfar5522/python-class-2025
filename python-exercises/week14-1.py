try:
    import sys
    import os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "lib")))
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "classes")))

    import animal
    import paycheck
   
except ModuleNotFoundError as e:
    print(
        f"{e}! Please ensure the module is named correctly and either:\n"
        "  - In the same directory as this program, or\n"
        "  - In the 'lib' or 'classes' folder one level above this program's directory.\n"
        "To use my file system setup, download it from: https://github.com/jfar5522/python-class-2025")
    sys.exit(f"Import failure! {e} available!")

print(animal.Animal(5,5,5))

clifford = animal.Dog(174165, 25, 5)

print(clifford)

# check1 = paycheck.Paycheck(5.00)
# print(check1)

check1 = paycheck.Paycheck(5000.00)
check2 = paycheck.Paycheck(5.00)
check3 = paycheck.Paycheck(1000.00)
check1 + check2
check1 + check3
print(check1)

check1 - check2
check1 - check3
check1 - check2
check1 - check3
print(check1)


if(isinstance(clifford, animal.Animal)):
    print('YES')

if(isinstance(clifford, animal.Dog)):
    print('YES')

if(hasattr(clifford, 'height')):
    print("yus")
