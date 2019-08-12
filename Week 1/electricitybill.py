TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

def electricity_bill_v1():
    print("Electricity Bill Estimator V1.0")
    cents_per_kwh = float(input("Enter Cents per kWh: "))
    use_in_kwh = float(input("Enter Daily use in kWh: "))
    days = float(input("Enter Billing Days"))
    total = (use_in_kwh*(cents_per_kwh/100))*days
    print("Estimated Bill: $",total)

def electricity_bill_v2():
    print("Electricity Bill Estimator V2.0")
    tariff= int(input("Which Tariff 11 or 31: "))
    use_in_kwh = float(input("Enter Daily use in kWh: "))
    days = float(input("Enter Billing Days"))
    if(tariff == 11):
        total = use_in_kwh*days*TARIFF_11
    elif(tariff == 31):
        total = use_in_kwh*days*TARIFF_31
    print("Estimated Bill: $",total)

def main():
    electricity_bill_v1()
    electricity_bill_v2()

if __name__ == "__main__":
    main()