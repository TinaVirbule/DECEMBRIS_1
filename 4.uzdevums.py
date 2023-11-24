def faktorials(skaitlis):
    rezultats = 1
    for i in range(1, skaitlis + 1):
        rezultats *= i
    return rezultats

ievaditais_skailtlis = int(input("ievadiet skaitli, kuram aprēķinat faktoriālu: "))

if ievaditais_skailtlis < 0:
    print("nebūs, mēģiniet vēlreiz")
else:
    rezultats = faktorials(ievaditais_skailtlis)
    print(f"faktoriāls no {ievaditais_skailtlis} ir {rezultats}, ko tik nevar uzzināt no matemātikas programmēšanā")