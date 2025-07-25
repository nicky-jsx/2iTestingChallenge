def find_largest_sum(array):

    if array is None:
        raise TypeError("Input cannot be empty")

    if not isinstance(array, list):
        raise ValueError("Input must be a list")

    if len(array) > 10:
        raise ValueError("List cannot have more than 10 strings")

    max_sum = 0

    for i, string in enumerate(array):
        #Validates that each element is a string
        if not isinstance(string, str):
            raise ValueError(f"Element at index {i} must be a string, got {type(string).__name__}")

        #Checks string length constraint
        if len(string) > 12:
            raise ValueError(f"String at index {i} cannot be longer than 12 characters")

        digits = [int(char) for char in string if char.isdigit()]
        current_sum = sum(digits)

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum


def test_function():
    #Test the function with various inputs

    test_cases = [
        #Basic test cases
        (["abc123def", "xyz456", "pqr789"], 24),
        (["hello", "world", "test"], 0),
        (["a1b2c3", "x4y5z6", "p7q8r9"], 24),

        #Edge cases
        ([], 0),  #Empty array
        ([""], 0),  #Empty string
        (["123456789"], 45),  #Single string with many digits
        (["a", "b", "c"], 0),  #Only letters

        #Example test case from brief
        (["dh7js4jf", "or2rjvn2w", "h1n36mfl", "a7e6fw"], 13),
    ]

    error_test_cases = [
        (None, TypeError, "Input cannot be empty"),
        ("not a list", ValueError, "Input must be a list"),
        (123, ValueError, "Input must be a list"),
        (["abc", 123, "def"], ValueError, "Element at index 1 must be a string"),
        (["abc", None, "def"], ValueError, "Element at index 1 must be a string"),
        (["abc"] * 11, ValueError, "List cannot have more than 10 strings"),
        (["a" * 13], ValueError, "String at index 0 cannot be longer than 12 characters"),
    ]

    print("Testing find_largest_sum function:")
    print("=" * 50)

    all_passed = True

    # Test normal cases
    print("Normal test cases:")
    for i, (input_strings, expected) in enumerate(test_cases, 1):
        result = find_largest_sum(input_strings)

        if result == expected:
            print(f"Test {i}: :) PASS")
        else:
            print(f"Test {i}: X FAIL")
            print(f"  Input: {input_strings}")
            print(f"  Expected: {expected}, Got: {result}")
            all_passed = False

    print("\nError handling test cases:")
    # Test error cases
    for i, (input_data, expected_exception, expected_message) in enumerate(error_test_cases, 1):
        try:
            result = find_largest_sum(input_data)
            print(f"Error Test {i}: X FAIL - Expected {expected_exception.__name__} but got result: {result}")
            all_passed = False
        except Exception as e:
            if isinstance(e, expected_exception) and expected_message in str(e):
                print(f"Error Test {i}: :) PASS - Correctly raised {expected_exception.__name__}")
            else:
                print(f"Error Test {i}: x FAIL - Expected {expected_exception.__name__} with message containing '{expected_message}', but got {type(e).__name__}: {e}")
                all_passed = False

    print("=" * 50)
    if all_passed:
        print("All tests passed! :)")
    else:
        print("Some tests failed! x")

    return all_passed


if __name__ == "__main__":
    # Run tests
    test_function()

    print("\n" + "=" * 50)
    print("Example usage:")
    print("=" * 50)

    #Example input from brief
    example_input = ["dh7js4jf", "or2rjvn2w", "h1n36mfl", "a7e6fw"]
    result = find_largest_sum(example_input)

    print(f"Input: {example_input}")
    print(f"Result: {result}")

    #Shows the breakdown
    print("\nBreakdown:")
    for string in example_input:
        digits = [int(char) for char in string if char.isdigit()]
        digit_sum = sum(digits)
        print(f"'{string}' -> digits: {digits} -> sum: {digit_sum}")

    print(f"\nMaximum sum: {result}")