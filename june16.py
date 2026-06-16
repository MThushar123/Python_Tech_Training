def strongPasswordChecker(password):
    n = len(password)

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)

    missing_types = 3 - (has_lower + has_upper + has_digit)

    replace = 0
    one_mod = 0
    two_mod = 0

    i = 0
    while i < n:
        j = i
        while j < n and password[j] == password[i]:
            j += 1

        length = j - i

        if length >= 3:
            replace += length // 3

            if length % 3 == 0:
                one_mod += 1
            elif length % 3 == 1:
                two_mod += 1

        i = j

    if n < 6:
        return max(missing_types, 6 - n)

    if n <= 20:
        return max(missing_types, replace)

    delete = n - 20
    remaining_delete = delete

    use = min(remaining_delete, one_mod)
    replace -= use
    remaining_delete -= use

    use = min(remaining_delete, two_mod * 2)
    replace -= use // 2
    remaining_delete -= use

    replace -= remaining_delete // 3

    return delete + max(missing_types, replace)

password = input("Enter password: ")

result = strongPasswordChecker(password)

print("Minimum Changes Required:", result)