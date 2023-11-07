from lorem_text import lorem

def analysis_text(text):
    # словарь для хранения частот символов
    frequency = {}
    # Подсчитываем общее число символов в тексте
    count_symbols = len(text)
    # Проходимся по каждому символу в тексте
    for symbol in text:
        if symbol in frequency:
            frequency[symbol] += 1
        else:
            frequency[symbol] = 1
    # Преобразуем частоты символов в пары (символ, частота встречаемости)
    result = [(symbol, frequency / count_symbols) for symbol, frequency in frequency.items()]
    return result

def hand_text():
    return

def auto_text():
    return

def menu():
    text = ""
    while True:
        print("Главное меню:")
        print("1. Ввести текст вручную.")
        print("2. Ввести текст случайным образом.")
        print("3. Решение задачи.")
        print("4. Выход из программы ")
        choose = input("Выберите пункт меню: ")

        if choose == "1":
            pass
        elif choose == "2":
            pass
        elif choose == "3":
            result = analysis_text(text)
            for symbol, frequency in result:
                print(f"{symbol} - {frequency:.4f}")
            input("Нажмите Enter, чтобы продолжить...")
        elif choose == "4":
            print("Выход из программы.")
            break
        else:
           print("Некорректный выбор. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    menu()
