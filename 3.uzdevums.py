skaitlis = int(input("ievadiet skaitli: "))

if skaitlis % 3 == 0 and skaitlis % 7 == 0:
    print(f"{skaitlis} dalās ar 3 un 7.")
else:
    print(f"{skaitlis} nedalās ar 3 un 7 vai dalot paliek atlikums, kas nozīmē,ka jāmēģina vēlreiz")

