# Shrinking Guest List
guests = ["Spongebob", "Patrick", "Squidward"]

person = guests[2].title()
print(f"{person}, Won't make it to the Krusty Krab tonight.\n")

guests[2] = "Squilliam"
guests.insert(0, "Garry")
guests.insert(2, "Sandy")
guests.append("Mrs. Pops")

person = guests[0].title()
print(f"{person}, Let's have a dinner at the Krusty Krab")

person = guests[1].title()
print(f"{person}, Let's have a dinner at the Krusty Krab")

person = guests[2].title()
print(f"{person}, Let's have a dinner at the Krusty Krab")

person = guests[3].title()
print(f"{person}, Let's have a dinner at the Krusty Krab")

person = guests[4].title()
print(f"{person}, Let's have a dinner at the Krusty Krab")

person = guests[5].title()
print(f"{person}, Let's have a dinner at the Krusty Krab")

print("\nDue to an unfortunate event, the Krusty Krab won't be accepting customers tonight.")
print("The event will be moved to Dorsia, and I can only invite two people.\n")

person = guests [-1]
guests.pop()
print(f"{person} I'm sorry I cannot invite you to dinner tonight.")

person = guests [-1]
guests.pop()
print(f"{person} I'm sorry I cannot invite you to dinner tonight.")

person = guests [-1]
guests.pop()
print(f"{person} I'm sorry I cannot invite you to dinner tonight.")

person = guests [-1]
guests.pop()
print(f"{person} I'm sorry I cannot invite you to dinner tonight.\n")

print(f"{guests[0]} you're still invited to a Dinner at Dorsia tonight")

print(f"{guests[1]} you're still invited to a Dinner at Dorsia tonight")