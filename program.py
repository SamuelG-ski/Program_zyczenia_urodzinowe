print("Witaj w prgramie spersonalizowanych życzeń urodzinowych!")

print()
print("Podaj imię odbiorcy:")
recipient_name = input()

print()
print("Podaj rok urodzenia odbiorcy:")
year_born = int(input())

print()
print("Podaj spersonalizowaną wiadomość:")
personalized_message = input()

print()
print("Podaj imię nadawcy:")
sender_name = input()

actual_year = int(2024)

age = actual_year - year_born

print()
print(f"{recipient_name}, wszystkiego najlepszego z okazji {age} urodzin!")

print()
print(f"{personalized_message}")

print()
print(f"{sender_name}")