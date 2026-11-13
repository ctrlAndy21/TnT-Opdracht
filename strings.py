student = " I am a student"

print(type(student))
print(student.index("a"))
print(student.count("a"))
print(student.find("stu"))
print(student.find("Stu"))
print(student.lower())
print(student.upper())
print(student.startswith(" "))
print(student.startswith("i"))
print(student.endswith("t"))
print(student.strip())
print(student.strip("t"))
print(len(student))

my_string = "Als een potvis in een pispot pist zit de pispot vol met potvispis. "
print(my_string[-2])

my_string2 = "De koetsier poetst de postkoets met postkoetspoets."
print(my_string2.count("o"))

my_string3 = "Als kakkerlakken in kattebakken kakken, heb je een kattebak vol met kakkerlakkak."
print(my_string3.replace(" ","_"))

my_string_1 = "Knappe kappers kappen knap,"
my_string_2 = "maar de knecht van de knappe kapper kapt"
my_string_3 = "nog knapper dan de knappe kapper kappen kan."

print(my_string_1 +" "+my_string_2 +" "+ my_string_3)