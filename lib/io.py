def ReadPasswordsAndLogins():
    """Read passwords and logins and return it in the dictionary"""
    dict = {}
    with open(".user_info.txt") as f:
        for line in f.readlines():
            words = line.split()
            dict[words[0]] = words[1]

    return dict
