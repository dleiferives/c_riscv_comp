import subprocess

def run_test(test_statement, file="temp_test.s"):
    # open the file, overwirtes the file if it already exists
    with open(file, "w") as f:
        f.write(test_statement)

    # run the compiler with the file collect the output
    output = subprocess.run(["../bin/c_riscv_comp.o", file], capture_output=True)

    with open(file, "w") as f:
        f.write(output.stdout.decode("utf-8"))

    # run the file with rars java -jar ./rars/rars_27a7c1f.jar file
    subprocess.run(["java", "-jar", "./rars/rars_27a7c1f.jar", file])

tests = {
        "addition": [
            ("1 + 1","1"),
            ("2 + 2","4"),
            ("3 + 3","6"),
            ("4 + 4","8"),
            ("5 + 5","10"),
            ("6 + 6","12"),
            ("7 + 7","14"),
            ("8 + 8","16"),
            ("9 + 9","18"),
            ("10 + 10","20")
            ]
        }
# for key in tests:


