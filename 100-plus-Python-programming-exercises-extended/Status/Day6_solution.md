A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

Following are the criteria for checking the password:

At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

Example

If the following passwords are given as input to the program:

ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:

ABd1234@1

```
def checkpass():
    goodpasswords = []
    passwords = input().split(',')
    for password in passwords:
        alpha_lower = sum([1 for x in password if x.islower()]) >= 1
        alpha_upper = sum([1 for x in password if x.isupper()]) >= 1
        numeric = sum([1 for x in password if x.isnumeric()]) >= 1
        symb = sum([1 for x in password if x in ['$','#','@']]) >= 1
        length = len(password) >= 6 and len(password) <= 12
        if alpha_lower and alpha_upper and numeric and symb and length:
            goodpasswords.append(password)
    print(','.join(goodpasswords))

```

---


