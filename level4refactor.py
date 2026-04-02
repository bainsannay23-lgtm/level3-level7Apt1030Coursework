def calculate_claim_procedural(amount):
    return amount * 0.90

patient_name = "Jane Doe"
patient_policy = "NHIF1234"
print(f"Approved Claim: {calculate_claim_procedural(5000)}")