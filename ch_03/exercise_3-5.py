# Changing Guest List
guests = ["Spongebob", "Patrick", "Squidward"]

person = guests[2].title()
print(f"{person}, Won't make it to the Krusty Krab tonight.")

person = guests[0].title()
print(f"\n{person}, Let's have a dinner at the Krusty Krab")

person = guests[1].title()
print(f"{person}, Let's have a dinner at the Krusty Krab")

guests[2] = "Squilliam".title()
print(f"{guests[2]}, Let's have a dinner at the Krusty Krab")