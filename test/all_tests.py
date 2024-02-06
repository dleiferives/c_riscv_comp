import subprocess

def run_test(test_statement, file="temp_test.s", display_individual_results=False):
    # open the file, overwirtes the file if it already exists
    with open(file, "w") as f:
        f.write(test_statement[0])

    # run the compiler with the file collect the output
    output = subprocess.run(["../bin/c_riscv_comp", file], capture_output=True)

    with open(file, "w") as f:
        f.write(output.stdout.decode("utf-8"))

    # run the file with rars java -jar ./rars/rars_27a7c1f.jar file
    output = subprocess.run(["java", "-jar", "./rars/rars_27a7c1f.jar", "me", file], capture_output=True)
    if(output.stdout.decode("utf-8") == test_statement[1]):
        if display_individual_results:
            print("Passed:", test_statement[0], "=>", test_statement[1])
        return True;
    if(display_individual_results):
        print("Failed:", test_statement[0], "=>", test_statement[1])
    return False;

def run_all_tests(tests, display_individual_results=False):
    for key in tests:
        failed_tests = []
        for test in tests[key]:
            if not run_test(test, display_individual_results=display_individual_results):
                failed_tests.append(test)
        # print the number of failed tests failed/all
        print("Failed", len(failed_tests), "/", len(tests[key]), "tests for", key)
        if len(failed_tests) > 0:
            print("Failed tests for", key)
            for test in failed_tests:
                print(test[0], "=>", test[1])

tests = {
        "Addition": [
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

run_all_tests(tests)

# for key in tests:


