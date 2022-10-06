def timeInWords(h, m):
    dic = {
        0 : "o' ",
        1 : "one",
        2 : "two",
        3 : "three",
        4 : "four",
        5 : "five",
        6 : "six",
        7 : "seven",
        8 : "eight",
        9 : "nine",
        10 : "ten",
        11 : "eleven",
        12 : "twelve",
        13 : "thirteen",
        14 : "fourteen",
        15 : "quarter",
        16 : "sixteen",
        17 : "seventeen",
        18 : "eighteen",
        19 : "nineteen",
        20 : "twenty",
        21 : "twenty one",
        22 : "twenty two",
        23 : "twenty three",
        24 : "twenty four",
        25 : "twenty five",
        26 : "twenty six",
        27 : "twenty seven",
        28 : "twenty eight",
        29 : "twenty nine",
        30 : "half",
        31: "thirty one",
        32: "thirty two",
        33: "thirty three",
        34: "thirty four",
        35: "thirty five",
        36: "thirty six",
        37: "thirty seven",
        38: "thirty eight",
        39: "thirty nine",
        40: "forty",
        41: "forty two",
        42: "forty two",
        43: "forty three",
        44: "forty four",
        45: "quarter",
        46: "forty six",
        47: "forty seven",
        48: "forty eight",
        49: "forty nine",
        50: "fifty",
        51: "fifty one",
        52: "fifty two",
        53: "fifty three",
        54: "fifty four",
        55: "fifty five",
        56: "fifty six",
        57: "fifty seven",
        58: "fifty eight",
        59: "fifty nine",

    }
    if m == 0:
        return f"{dic[h]} o' clock"
    if m == 1:
        return f"{dic[h]} minute past {dic[h]}"
    elif m == 15:
        return f"{dic[m]} past {dic[h]}"
    elif m == 30:
        return f"{dic[m]} past {dic[h]}"
    elif m < 30:
        return f"{dic[m]} minutes past {dic[h]}"
    elif m == 45:
        h += 1
        return f"{dic[m]} to {dic[h]}"
    else:
        m = 60 - m
        h +=1
        return f"{dic[m]} minutes to {dic[h]}"


if __name__ == '__main__':
    h = 1
    m = 1
    result = timeInWords(h, m)
    print(result)