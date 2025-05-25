class Bank:
    bank_name = "Habib"

    def change_bank_name(cls, name):
        cls.bank_name = new_bank_name

Bank.change_bank_name = ("meezan")
print(Bank.change_bank_name)

print(Bank.bank_name)

