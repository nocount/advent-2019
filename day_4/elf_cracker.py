# Solution for Day 4 of Advent of Code 2019


def is_valid_password(password):

    has_dupe = False
    # Check descending
    for i in range(1, 6):
        if int(password[i]) < int(password[i-1]):
            return False

    # Check dupes
    counts = [password.count(c) for c in set(password)]
    for c in counts:
        if c == 2:
            has_dupe = True

    if has_dupe:
        return True
    else:
        return False


if __name__ == '__main__':

    count = 0
    for p in range(136760, 595731):

        if is_valid_password(str(p)):
            count += 1

    print(count)
