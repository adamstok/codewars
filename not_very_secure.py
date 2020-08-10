"""
In this example you have to validate if a user input string is alphanumeric. The given string is not nil/null/NULL/None, so you don't have to check that.

The string has the following conditions to be alphanumeric:

At least one character ("" is not valid)
Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
No whitespaces / underscore


"""

def alphanumeric(password):
    tf_list = [x.isalnum() for x in password]
    utf8 = []
    for l in password:
        utf8.append(len(l.encode('utf-8')))
    if False in tf_list or 1 not in utf8:
        return False
    return True


@test.describe("Sample Tests")
def sample_tests():
        tests = [
            ("hello world_", False),
            ("PassW0rd", True),
            ("     ", False)
        ]
        for s, b in tests:
            @test.it('alphanumeric("' + s + '")')
            def sample_test():
                Test.assert_equals(alphanumeric(s), b)
