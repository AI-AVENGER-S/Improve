import json
import matplotlib.pyplot as plt

def main():
    with open("data_mat_model.json", "r") as file:
        records_mat = json.load(file)

    with open("data_flight_final.json", "r") as file:
        records_ksp = json.load(file)

    plt.subplot(2, 1, 1)
    plt.plot(records_ksp[2], records_ksp[0], label="KSP")
    plt.plot(records_mat[2], records_mat[0], label="Mat")
    plt.xlabel('Время, с') #Подпись для оси х
    plt.ylabel('Высота от уровня моря, м') #Подпись для оси y
    plt.title('График зависимости высоты от времени') #Название
    plt.legend(fontsize=9)

    plt.subplot(2, 1, 2)
    plt.plot(records_ksp[2], records_ksp[1], label="KSP")
    plt.plot(records_mat[2], records_mat[1], label="Mat")
    plt.xlabel('Время, с') #Подпись для оси х
    plt.ylabel('Скорость ракеты, м/c') #Подпись для оси y
    plt.title('График зависимости скорости от времени') #Название
    plt.legend(fontsize=9)
    plt.show()

if __name__ == "__main__":
    main()
