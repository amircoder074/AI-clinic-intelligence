# it checks the index of any darmangar and moraje #

@staticmethod
def barresi_code(code : str):
    if len(code) != 10 or not code.isdigit():
        raise ValueError("Code bayad yek adad 10 raghami bashad.")
    if len(set(code)) == 1: 
        raise ValueError("Code nabayad daraye adad yeksan bashad.")
    total = sum(int(digit) * (10 - index) for index, digit in enumerate(code[:-1]))
    reminder = total % 11

    check_digit = int(code[-1])
    try : 
        if (reminder < 2 and check_digit == reminder) or (reminder >= 2 and check_digit == 11 - reminder):
            raise Exception
    except Exception : 
        print("Code vared shode motabar hast..:)")
    else : 
        return True