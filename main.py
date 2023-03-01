from dataclasses import dataclass


@dataclass(slots=True)
class Data:
    name: str
    hours: list[int]
    sum_hours: int


def write_file(filename: str) -> list[tuple]:
    with open(filename, encoding='utf-8') as file:
        data = [(' '.join(line.split()[:-1]), line.split()[-1]) for line in file if line != "\n"]
        return data


def get_statistic(data: list[tuple]) -> dict[Data]:
    result_data = {}
    for elem in data:
        name = elem[0]
        hours = int(elem[1])
        if name in result_data:
            result_data[name].hours.append(hours)
            result_data[name].sum_hours = sum(result_data[name].hours)
        else:
            result_data[name] = Data(name=name, hours=[hours], sum_hours=hours)

    return result_data


def print_data(result_data: dict[Data]) -> None:
    for name, data in result_data.items():
        hours = [str(h) for h in data.hours]
        print(f'{data.name}: {", ".join(hours)}, sum: {data.sum_hours}')


def run():
    data = write_file('data.txt')
    res = get_statistic(data)
    print_data(res)


if __name__ == '__main__':
    run()
