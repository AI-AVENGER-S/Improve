import json
import matplotlib.pyplot as plt

def main():
    with open("sous 2_1B calculations/data_mat_model_sous.json", "r") as file:
        records_sous = json.load(file)

    with open("Vostok-1 calculations/data_mat_model.json", "r") as file:
        records_vostok = json.load(file)

    plt.subplot(2, 1, 1)
    plt.plot(records_sous[2], records_sous[0], label="Союз 2.1б")
    plt.plot(records_vostok[2], records_vostok[0], label="Восток 1")
    plt.xlabel('Время, с') #Подпись для оси х
    plt.ylabel('Высота от уровня моря, м') #Подпись для оси y
    plt.title('График зависимости высоты от времени') #Название
    plt.legend(fontsize=9)

    plt.subplot(2, 1, 2)
    plt.plot(records_sous[2], records_sous[1], label="Союз 2.1б")
    plt.plot(records_vostok[2], records_vostok[1], label="Восток 1")
    plt.xlabel('Время, с') #Подпись для оси х
    plt.ylabel('Скорость ракеты, м/c') #Подпись для оси y
    plt.title('График зависимости скорости от времени') #Название
    plt.legend(fontsize=9)
    plt.show()

if __name__ == "__main__":
    main()
