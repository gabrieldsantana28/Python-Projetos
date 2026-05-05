# for cont_ex in range(1,6):
#     print(f"\nRodada: {cont_ex}")
#     for cont_in in range(5, 0, -1):
#         print(f"Valor: {cont_in}")

# print("Fim dos laços")

import random as rd

for a in range(1,6):
    print(f"Conjunto {a}")
    for b in range(5):
        num = rd.randint(1,100)
        print(f"Valor: {num}")