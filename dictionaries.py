my_dict = {"Vendor":"Cisco", "Device":"3750", "Ports":"24", "IOS":"13"}

print(type(my_dict))
print(len(my_dict))
del my_dict["Ports"]
print(my_dict)
my_dict["RAM"] = 256
print(my_dict)
print("Vendor" in my_dict)
print("vendor" in my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
my_dict.pop('Device')
print(my_dict)
my_dict.update({"Speed" : "1Gb"})
print(my_dict)

scripting_languages = {1: "python", 2: "ruby", 3: "javascript", 4: "PHP", 5: "perl"}
ide_programs = {"ide_atom": "atom", "ide_vs": "visual_studio", "ide_pv": "py_dev", "ide_pc": "pyCharm"}

print(type(scripting_languages))
print(type(ide_programs))

print(scripting_languages[3])
print(ide_programs["ide_pv"])

print(scripting_languages.get(1))
print(ide_programs.get("ide_pc"))

scripting_languages[4] = "Bash"
print(scripting_languages)
#5. Maak een nieuwe item met als key "ide_rm" en als value "rubeMine" aan voor de variabele “ide_programs”
ide_programs.update({"ide_rm" : "rubeMine"})
print(ide_programs)
#6. Verwijder de key en value visual_studio van de variabele ide_programs
#Tip: Maak gebruik van del
del ide_programs["ide_vs"]
print(ide_programs)
#7. Verwijder de key en value perl van de variabele scripting_languages op basis van key
#Tip: Maak gebruik van pop
scripting_languages.pop(5)
print(scripting_languages)
#8. Maak een nieuwe variabele "scripting_values" aan en doe het volgende:
#• Zorg dat enkel de values van de variabele scripting_languages worden bewaard in
#scripting_values en weergeef deze terug op het scherm
#• Toon de class van scripting_values
#• Converteer de class van scripting_values naar een list en toon deze nadien op het scherm
scripting_values = scripting_languages.values()
print(scripting_values)
print(type(scripting_values))
scripting_values = list(scripting_values)
print(scripting_values)
print(type(scripting_values))
#9. Maak een nieuwe variabele "program_keys" aan en doe het volgende:
#• Zorg dat enkel de keys van de variabele ide_programs worden bewaard in program_keys en
#weergeef deze terug op het scherm
#• Toon de class van program_keys
#• Converteer de class van program_keys naar een list en toon deze nadien op het scherm
program_keys = ide_programs.keys()
print(program_keys)
print(type(program_keys))
program_keys = list(program_keys)
print(program_keys)
