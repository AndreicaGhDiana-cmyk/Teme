text="Autumn carries more gold in its pocket, than all the other seasons."
mijloc=len(text)//2
prima_parte=text[:mijloc].upper().strip()
a_doua_parte=text[mijloc::-1].capitalize().replace(",","").replace(".","")
print(prima_parte+a_doua_parte)
