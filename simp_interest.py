

def sim_interest(principal, time , rate):
    return (principal * time * rate) / 100

if __name__ == "__main__":
    p=int(input("Enter principal amount: "))
    t=int(input("Enter time in years: "))
    r=int(input("Enter rate of interest: "))

    print("Simple interest: ", sim_interest(p, t, r))
    