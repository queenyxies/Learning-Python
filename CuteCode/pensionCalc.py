class PensionCalculator:
    def __init__(self, years_of_service, final_salary, accrual_rate):
        self.years_of_service = years_of_service
        self.final_salary = final_salary
        self.accrual_rate = accrual_rate

    def calculate_pension(self):
        return self.years_of_service * self.final_salary * self.accrual_rate


# Example usage:
years_of_service = 30
final_salary = 50000  # Final salary in dollars
accrual_rate = 0.015  # 1.5% accrual rate

pension_calculator = PensionCalculator(years_of_service, final_salary, accrual_rate)
annual_pension = pension_calculator.calculate_pension()

print(f"Annual Pension: ${annual_pension:.2f}")

class Dog:
    species = "Canis familiaris"  # Class variable

    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

dog1 = Dog("Buddy", 5)
dog2 = Dog("Max", 7)

print(dog1.species)  # Output: Canis familiaris
print(dog2.species)  # Output: Canis familiaris
print(Dog.species)
