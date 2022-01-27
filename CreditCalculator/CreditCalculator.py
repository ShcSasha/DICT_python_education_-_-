import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--principal')
parser.add_argument('--interest')
parser.add_argument('--annuity')
parser.add_argument('--payment')
parser.add_argument('--periods')
arg = parser.parse_args()

type = arg.type
principal = arg.principal
interest1 = arg.interest
annuity = arg.annuity
payment = arg.payment
periods = arg.periods

print(principal, interest1, annuity, periods, payment, type)


# A?
def func1():
    p = int(principal)
    per = int(periods)
    percent = float(interest1)
    interest = percent / (12 * 100)
    print(interest)
    annuity = p * ((interest * pow((1 + interest), per)) / (pow((1 + interest), per) - 1))
    over = math.ceil(annuity) * per - p
    print(f'Your annuity payment = {math.ceil(annuity)}!')
    print(f'Overpayment = {over}')


# n
def func2():
    p = int(principal)
    pay1 = int(payment)
    percent = float(interest1)
    interest = percent / (12 * 100)
    if percent:
        i = interest
        print(i)
        x = int(pay1) / (int(pay1) - (interest / 1200 * int(p)))
        print(x)
        degree = math.log(int(pay1) / (int(pay1) - (i * p)), (1 + i))
        year = math.ceil(degree) / 12
        r = str(round(year, 1))
        print("It will take", list(r)[0], "years and", list(r)[2], "months to repay this loan!")
        print("Overpayment =", p * math.ceil(degree) - int(p))
    else:
        print("Incorrect Par8")


# P
def func3():
    per = float(periods)
    pay2 = float(payment)
    percent = float(interest1)
    #interest = percent / (12 * 100)
    if percent != interest1:
        percent = float(interest1)
        i = percent / (12 * 100)
        num = pow(1 + i, float(per))
        a = i * (1 + i) ** float(per)
        print(a)
        b = (1 + i) ** float(per) - 1
        print(b)
        c = a / b
        print(c)
        d = float(pay2) / c
        result_p = math.floor(float(float(payment) / ((i * num) / (num - 1))))
        print("Your loan principal =", round(d), "!")
        print('Overpayment =', float(pay2) * float(per) - result_p)
    else:
        print("Incorrect Par13")


# D
def func4(P, n, inter):
    # pri = float(principal)
    # per = float(periods)
    # inter1 = float(interest1)
    i = inter / (100 * 12)
    total = 0
    for m in range(1, n + 1):
        D = P / n + i * (P - P * (m - 1) / n)
        total += math.ceil(D)
        print(f'Month {m}: paid out {math.ceil(D)}')
        print()
        over = total - P
        print(f'Overpayment = {over}')


if __name__ == "__main__":
    if type == "annuity":
        if principal and interest1 and periods:
            func1()
        elif principal and payment and interest1:
            func2()
        elif periods and payment and interest1:
            func3()
        else:
            print("Incorrect parameters")
    elif type == "diff":
        if principal and periods and interest1:
            func4(principal, periods, interest1)
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")
