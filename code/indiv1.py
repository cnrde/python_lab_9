import sys

if __name__ == '__main__':
    airport = []
    while True:
        command = input(">>> ").lower()
        if command == 'exit':
            break

        elif command == 'add':
            race = input("Название пункта назначения рейса ")
            number = input("Номер рейса ")
            type = input("Тип самолёта ")

            airports = {
                'race': race,
                'number': number,
                'type': type,
            }

            airport.append(airports)
            if len(airport) > 1:
                airport.sort(key=lambda item: item.get('race', ''))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 20
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                    "No",
                    "Пункт",
                    "Номер",
                    "Тип самолёта."
                )
            )
            print(line)
            for idx, airports in enumerate(airport, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                        idx,
                        airports.get('race', ''),
                        airports.get('number', ''),
                        airports.get('type', 0)
                    )
                )

            print(line)

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=2)
            sel = (parts[1])

            count = 0
            for airports in airport:
                if airports.get('race') == sel:
                    count += 1
                    print(
                        '{:>4}: {}'.format(count, airports.get('race', ''))
                    )
                    print('Номер рейса:', airports.get('number', ''))
                    print('Тип самолёта:', airports.get('type', ''))

            if count == 0:
                print("Рейс не найден.")

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить рейс;")
            print("list - вывести список рейсов;")
            print("select <товар> - информация о рейсе;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print("Неизвестная команда {command}", file=sys.stderr)