from calculation import thing

while True:
    try:
        thing()
        break
    except ValueError:
        print("Invalid input. Please enter valid numeric values for x and y.")