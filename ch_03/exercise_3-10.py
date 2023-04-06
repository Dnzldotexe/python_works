# Every Function
languages = ["HTML", "Java", "CSS", "JavaScript", "C", "SQL", "R",]

print(languages[0].title())

languages.append("Python")
print(languages)

languages.insert(-2, "VBA")
print(languages)

del languages[-3]
print(languages)

languages.pop(0)
print(languages)

languages.remove("CSS")
print(languages)

lang = ["HTML", "Java", "CSS", "JavaScript", "C", "SQL", "R",]

lang.sort(reverse = True)
print(lang)

print(sorted(languages))

print(languages)

lang.reverse()
print(lang)