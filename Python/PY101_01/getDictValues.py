courses = {
    "js" : "Javascript 101",
    "python" : ["Python 101", "Python 202"],
    "HTML" : "HTML 101"
}

print(courses)
print(courses["js"])


print(courses.get("css", None))


if courses.get("css", None):
    print(courses.get("css", "CSS 101"))