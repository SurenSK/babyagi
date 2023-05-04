from dotenv import dotenv_values, set_key, load_dotenv
import subprocess
import os
from time import sleep
runs = [
        # ("Try finding 2+2(5*5)/2", "math01", "1"),
        # ("Calculate the square root of 256.", "math02", "1"),
        # ("Solve for x: 3x - 4 = 2x + 10.", "math03", "5"),
        # ("Find the perimeter of a rectangle with length 6 cm and width 8 cm.", "math04", "3"),
        # ("What is the slope of the line that passes through the points (2, 5) and (4, 9)?", "math05", "5"),
        # ("Simplify the expression: (2x^2 + 3x - 5) - (3x^2 - 2x + 1).", "math06", "5"),
        ("Evaluate the integral of 3x^2 + 2x + 1 with respect to x.", "math07", "5"),
        ("Create a new text file named 'example.txt' and write the string 'Hello, World!' to it.", "file01", "5"),
        ("Read the contents of a file named 'data.csv' and parse it into a list of dictionaries, where each dictionary represents a row of data.", "file02", "10"),
        ("Rename a file named 'old.txt' to 'new.txt'.", "file03", "3"),
        ("Write a Python script that copies all files from a source directory to a destination directory.", "file04", "10"),
        ("Delete a file named 'example.txt' from the file system.", "file05", "3"),
        ("Create a recipe book application that suggests meals based on available ingredients.", "food01", "10"),
        ("Create a fitness tracking application that allows users to set goals and track their progress over time.", "app01", "20"),
        ("Build a language learning app that uses AI-powered chatbots to simulate real-life conversation.", "app02", "20"),
        ("Pretend you are a qualified mathematics professor. Try finding 2+2(5*5)/2", "math01r", "5"),
        ("Pretend you are a mathematics expert. Calculate the square root of 256.", "math02r", "5"),
        ("Pretend you are a math teacher. Solve for x: 3x - 4 = 2x + 10.", "math03r", "5"),
        ("Pretend you are a geometry instructor. Find the perimeter of a rectangle with length 6 cm and width 8 cm.", "math04r", "3"),
        ("Pretend you are a math tutor. What is the slope of the line that passes through the points (2, 5) and (4, 9)?", "math05r", "5"),
        ("Pretend you are a math professor. Simplify the expression: (2x^2 + 3x - 5) - (3x^2 - 2x + 1).", "math06r", "5"),
        ("Pretend you are a calculus expert. Evaluate the integral of 3x^2 + 2x + 1 with respect to x.", "math07r", "5"),
        ("Pretend you are a computer science professor. Create a new text file named 'example.txt' and write the string 'Hello, World!' to it.", "file01r", "5"),
        ("Pretend you are a data analyst. Read the contents of a file named 'data.csv' and parse it into a list of dictionaries, where each dictionary represents a row of data.", "file02r", "10"),
        ("Pretend you are a system administrator. Rename a file named 'old.txt' to 'new.txt'.", "file03r", "3"),
        ("Pretend you are a software developer. Write a Python script that copies all files from a source directory to a destination directory.", "file04r", "10"),
        ("Pretend you are a computer technician. Delete a file named 'example.txt' from the file system.", "file05r", "3"),
        ("Pretend you are a chef. Create a recipe book application that suggests meals based on available ingredients.", "food01r", "10"),
        ("Pretend you are a personal trainer. Create a fitness tracking application that allows users to set goals and track their progress over time.", "app01r", "20"),
        ("Pretend you are a language expert. Build a language learning app that uses AI-powered chatbots to simulate real-life conversation.", "app02r", "20"),
        ("Try finding 2+2(55)/2. Make sure you can reason through the solution step by step.", "math01c", "5"),
        ("Calculate the square root of 256. Make sure you can reason through the solution step by step.", "math02c", "5"),
        ("Solve for x: 3x - 4 = 2x + 10. Make sure you can reason through the solution step by step.", "math03c", "5"),
        ("Find the perimeter of a rectangle with length 6 cm and width 8 cm. Make sure you can reason through the solution step by step.", "math04c", "3"),
        ("What is the slope of the line that passes through the points (2, 5) and (4, 9)? Make sure you can reason through the solution step by step.", "math05c", "5"),
        ("Simplify the expression: (2x^2 + 3x - 5) - (3x^2 - 2x + 1). Make sure you can reason through the solution step by step.", "math06c", "5"),
        ("Evaluate the integral of 3x^2 + 2x + 1 with respect to x. Make sure you can reason through the solution step by step.", "math07c", "5"),
        ("Create a new text file named 'example.txt' and write the string 'Hello, World!' to it. Make sure you can reason through the solution step by step.", "file01c", "5"),
        ("Read the contents of a file named 'data.csv' and parse it into a list of dictionaries, where each dictionary represents a row of data. Make sure you can reason through the solution step by step.", "file02c", "10"),
        ("Rename a file named 'old.txt' to 'new.txt'. Make sure you can reason through the solution step by step.", "file03c", "3"),
        ("Write a Python script that copies all files from a source directory to a destination directory. Make sure you can reason through the solution step by step.", "file04c", "10"),
        ("Delete a file named 'example.txt' from the file system. Make sure you can reason through the solution step by step.", "file05c", "3"),
        ("Create a recipe book application that suggests meals based on available ingredients. Make sure you can reason through the solution step by step.", "food01c", "10"),
        ("Create a fitness tracking application that allows users to set goals and track their progress over time. Make sure you can reason through the solution step by step.", "app01c", "20"),
        ("Build a language learning app that uses AI-powered chatbots to simulate real-life conversation. Make sure you can reason through the solution step by step.", "app02c", "20"),
        ("Pretend you are a qualified mathematics professor. Try finding 2+2(55)/2. Make sure you can reason through the solution step by step.", "math01rc", "5"),
        ("Pretend you are a mathematics expert. Calculate the square root of 256. Make sure you can reason through the solution step by step.", "math02rc", "5"),
        ("Pretend you are a math teacher. Solve for x: 3x - 4 = 2x + 10. Make sure you can reason through the solution step by step.", "math03rc", "5"),
        ("Pretend you are a geometry instructor. Find the perimeter of a rectangle with length 6 cm and width 8 cm. Make sure you can reason through the solution step by step.", "math04rc", "3"),
        ("Pretend you are a math tutor. What is the slope of the line that passes through the points (2, 5) and (4, 9)? Make sure you can reason through the solution step by step.", "math05rc", "5"),
        ("Pretend you are a math professor. Simplify the expression: (2x^2 + 3x - 5) - (3x^2 - 2x + 1). Make sure you can reason through the solution step by step.", "math06rc", "5"),
        ("Pretend you are a calculus expert. Evaluate the integral of 3x^2 + 2x + 1 with respect to x. Make sure you can reason through the solution step by step.", "math07rc", "5"),
        ("Pretend you are a computer science professor. Create a new text file named 'example.txt' and write the string 'Hello, World!' to it. Make sure you can reason through the solution step by step.", "file01rc", "5"),
        ("Pretend you are a data analyst. Read the contents of a file named 'data.csv' and parse it into a list of dictionaries, where each dictionary represents a row of data. Make sure you can reason through the solution step by step.", "file02rc", "10"),
        ("Pretend you are a system administrator. Rename a file named 'old.txt' to 'new.txt'. Make sure you can reason through the solution step by step.", "file03rc", "3"),
        ("Pretend you are a software developer. Write a Python script that copies all files from a source directory to a destination directory. Make sure you can reason through the solution step by step.", "file04rc", "10"),
        ("Pretend you are a computer technician. Delete a file named 'example.txt' from the file system. Make sure you can reason through the solution step by step.", "file05rc", "3"),
        ("Pretend you are a chef. Create a recipe book application that suggests meals based on available ingredients. Make sure you can reason through the solution step by step.", "food01rc", "10"),
        ("Pretend you are a personal trainer. Create a fitness tracking application that allows users to set goals and track their progress over time. Make sure you can reason through the solution step by step.", "app01rc", "20"),
        ("Pretend you are a language expert. Build a language learning app that uses AI-powered chatbots to simulate real-life conversation. Make sure you can reason through the solution step by step.", "app02rc", "20")
    ]

for objective, logName, iters in runs:
    os.environ["OBJECTIVE"] = objective
    os.environ["LOGNAME"] = logName
    os.environ["ITERS"] = str(iters)
    print(f"Running with {logName} for {iters} iterations...")

    # Call babyagi.py and wait for it to finish
    env_vars = {**os.environ}
    subprocess.run(["python", "babyagi.py"], env=env_vars)

    with open(f"logs/{logName}.log", "r") as f:
        lines = f.readlines()
    last_line = lines[-1].strip()

    if "ITERS EXHAUSTED" in last_line:
        res = "FAILURE"
    elif "OBJECTIVE ACCOMPLISHED" in last_line:
        res = "SUCCESS"
    else:
        res = "REFER TO LOG"

    # Write objective, logName, iters, success to a file
    with open("logs/results.txt", "a") as f:
        f.write(f"{objective}, {logName}, {iters}, {res}\n")