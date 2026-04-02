class Patient:
    def __init__(self, name, policy_number):
        self.name = name
        self.policy_number = policy_number
        
    def calculate_claim(self, amount):
        # Deduct 10% co-payment
        return amount * 0.90

patient1 = Patient("Jane Doe", "NHIF1234")
print(f"Approved Claim: {patient1.calculate_claim(5000)}")
