TARIFFS = {"11": 0.244618, "31": 0.136928, "34": 0.13645438}


def electricity_bill_v2():
    print("Electricity Bill Estimator V2.0")
    for keys in TARIFFS:
        print("TARIFF", keys)
    tariff_option = input("Which Tariff 11 or 31: ")
    use_in_kwh = float(input("Enter Daily use in kWh: "))
    days = float(input("Enter Billing Days: "))
    total = use_in_kwh*days*TARIFFS[tariff_option]
    print("Estimated Bill: ${:.2f}".format(total))


def main():
    electricity_bill_v2()

if __name__ == "__main__":
    main()
