sneigs = int(input("ievadiet skaitli (labāk veselu): "))

if sneigs < 1:
    print("es teicu veselu...VESELU SKAITLI *izelpa* mēģiniet vēlreiz")
else:
    summa = 0

    for skaitlis in range(1, sneigs + 1):
        summa += skaitlis

    print(f"summa no 1 līdz {sneigs} ir {summa}, forši ne? man ar tā liekas")