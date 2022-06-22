from replit import clear
import art

ans = True
print(art.logo)
print("Welcome to the secret auction program")
record={}
while (ans):
  name = input("What is your name ?")
  bid = int(input("what's your bid?"))
  record[name] = bid
  next = input("Are there any other bidders?Type 'yes' or 'no'")
  if next == "yes":
    ans = True
    clear()
  else :
    ans = False
    clear()
high = max(record, key=record.get)
print(f'The winner is {high} with the bid of ${record[high]}')
