import json


def validate_test_case():
    """
    :return: True if all required fields are present in the test_case.json. Otherwise, returns False.
    """

    with open("test_case5_claude_2.json") as f:
        test_case = json.load(f)

    missing_fields = []
    required_fields = ["name", "description", "corresponding NFR", "preconditions", "input data",
                       "metrics", "test result", "notes"]
    for field in required_fields:
        if field not in test_case.keys():
            missing_fields.append(field)

    if len(missing_fields) > 0:
        print("Fail")
    else:
        print("Pass")


if __name__ == "__main__":
    validate_test_case()
