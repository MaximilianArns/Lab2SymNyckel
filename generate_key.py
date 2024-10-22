from cryptography.fernet import Fernet

key = Fernet.generate_key()

print(key)

key_name = input("Skriv in namnet på nyckeln du vill skapa: ")

#Kontrollera om filnamnet slutar på ".key", lägger till det annars
if not key_name.endswith(".key"):
    key_name += ".key"

with open(key_name, "wb") as key_file:
    key_file.write(key)
print(f"Nyckeln har sparats som {key_name}")