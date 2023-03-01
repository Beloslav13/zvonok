
def get_data(filename: str) -> dict:
    data = {}
    with open(filename, encoding='utf-8') as file:
        for line in file:
            name, hours = ' '.join(line.split()[:-1]), int(line.split()[-1])
            if name in data:
                data[name]['hours'].append(hours)
                data[name]['sum_hours'] = sum(data[name]['hours'])
            else:
                data[name] = name
                data[name] = {'hours': [hours], 'sum_hours': hours}

    return data


def print_data(result_data: dict) -> None:
    for name, data in result_data.items():
        hours = [str(h) for h in data['hours']]
        print(f'{name}: {", ".join(hours)}, sum: {data["sum_hours"]}')


def run():
    data = get_data('data.txt')
    print_data(data)


if __name__ == '__main__':
    run()
