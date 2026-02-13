def simple_interest(principal, rate, time):
    # Formula: SI = (P × R × T) / 100
    si = (principal * rate * time) / 100
    return si

print("=== Simple Interest Calculator ===")
print("Formula: SI = (Principal × Rate × Time) / 100")

principal = float(input("Enter Principal amount (₹): "))
rate = float(input("Enter Rate of interest (%): "))
time = float(input("Enter Time (years): "))

interest = simple_interest(principal, rate, time)
total_amount = principal + interest

print(f"\n Results:")
print(f"Principal: ₹{principal:,.2f}")
print(f"Rate: {rate}%")
print(f"Time: {time} years")
print(f"Simple Interest: ₹{interest:,.2f}")
print(f"Total Amount: ₹{total_amount:,.2f}")
