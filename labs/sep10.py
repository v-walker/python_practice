chapters = ['Python', 'Javascript', "HTML/CSS", "Node", "React", "Redux"]

days = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]

for chap in chapters:
    print(chap)
    for day in days:
        if (day != "sat") and (day != "sun"):
            print(f"\t {day}")
