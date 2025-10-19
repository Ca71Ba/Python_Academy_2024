animals = ["cat", "dog", "rabbit", "hamster", "parrot"]
animals.append("fish")
animals.insert(2, "turtle")

print(animals)
print(f"Letztes Element: {animals[-1]}")
print(f"Anzahl der Tiere: {len(animals)}")

animals.sort(reverse=True)
print(f"Sortierte Liste: {animals}")

