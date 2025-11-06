# import test


def test_var():
    age = 30
    price = 19.99
    name = "Alice"
    is_active, is_no = True, False
    print(f"Age:{age}")
    print(f"is_active:{is_active}")
    print(f"is_no:{is_no}")

def test_operator():
    a, b = 10, 3
    sum_result = a + b
    diff_result = a - b
    prod_result = a * b
    div_result = a / b
    floor_div_result = a // b
    mod_result = a % b
    exp_result = a ** b
    print(f"Sum: {sum_result}, Diff: {diff_result}, Prod: {prod_result}, Div: {div_result}, Floor Div: {floor_div_result}, Mod: {mod_result}, Exp: {exp_result}")

def test_condition():
    x = 15
    if x > 10:
        print("x is greater than 10")
    elif x == 10:
        print("x is equal to 10")
    else:
        print("x is less than 10")

def test_loops():
    #for loop
    for i in range(5):
        print(f"Iteration {i}")

    #while loop
    count = 0
    while count < 5:
        print(f"Count {count}")
        count += 1

def test_collection():
    #list
    fruits = ["apple", 123]
    #tuple
    coordinates = (10.0, 20.0)
    #set
    unique_numbers = {1, 2, 3, 4, 5}
    #dictionary
    person = {"name": "Alice", "age": 30}
    print(f"Fruits: {fruits}")
    print(f"Coordinates: {coordinates}")
    print(f"Unique Numbers: {unique_numbers}")
    print(f"Person: {person}")


def test_loop_collection():
    # Loop through list
    colors = ["red", "green", "blue"]
    for color in colors:
        print(f"Color: {color}")
    
    # loop through list with index
    for index, color in enumerate(colors):
        print(f"Index: {index}, Color: {color}")

    # Loop through dictionary with key value pairs
    student = {"name": "Bob", "grade": "A"}
    for key, value in student.items():
        print(f"{key}: {value}")
    # Loop through dictionary keys
    for key in student.keys():
        print(f"Key: {key}")
    # Loop through dictionary values
    for value in student.values():
        print(f"Value: {value}")

    # Loop through set
    primes = {2, 3, 5, 7, 11}
    for prime in primes:
        print(f"Prime: {prime}")

def test_ops_collection():
    # List operations
    numbers = [1, 2, 3]
    numbers.append(4)
    numbers.remove(2)
    numbers.insert(1, 5)
    print(f"List after operations: {numbers}")

    # Tuple operations
    coords = (10, 20)
    print(f"Tuple length: {len(coords)}")

    # Set operations
    a = {1, 2, 3}
    b = {3, 4, 5}
    union_set = a.union(b)
    intersection_set = a.intersection(b)
    print(f"Union: {union_set}, Intersection: {intersection_set}")

    # Dictionary operations
    student = {"name": "Alice", "age": 25}
    student["grade"] = "A"
    del student["age"]
    print(f"Dictionary after operations: {student}")

if __name__ == "__main__":
    #test_var()
    #test_operator()
    #test_condition()
    # test_loops()
    # test_collection()
    # test_loop_collection()
    test_ops_collection() 
    print("Test function executed.")