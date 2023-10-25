from bank import bankaccount 



account_number = input("Dime tu número de cuenta")
account = bankaccount(account_number)


funds = float(input("¿Cuanto dinero  quieres añadir?"))
print(f"Hay {account.get_balance()}€ en tu cuenta")

account.add_funds(funds)
print(f"Ahora hay {account.get_balance()}€ en tu cuenta")
cuentas = []
cuentas[1] = bankaccount()