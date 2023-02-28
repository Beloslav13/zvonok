from typing import TypeAlias, NamedTuple


# Hours: TypeAlias = int


class Data(NamedTuple):
    name: str
    # hours: list[Hours]
    hours: list[int]
    sum_hours: int


def write_file(filename: str) -> list[tuple]:
    with open(filename, encoding='utf-8') as file:
        data = [(' '.join(line.split()[:-1]), line.split()[-1]) for line in file if line != "\n"]
        return data


def get_statistic(data: list[tuple]) -> list[Data]:
    list_data = []
    prepare_data = _prepare_data(data)

    # получилось длиннее из-за того что пришлось создавать еще объекты NamedTuple, предусмотрено для большой реализации
    # удобства, понятно какой тип возвращается, какие у него поля, и для возможной валидации этих полей...
    # в конечно итоге чтобы структура Data получилась чистой для след. взаимодействия: передачи куда либо, save и т.д.
    for k, v in prepare_data.items():
        sum_hours = v['sum_hours'] if v.get('sum_hours') else v['hours'][0]
        hours = v['hours']
        list_data.append(Data(name=k, hours=hours, sum_hours=sum_hours))

    return list_data


def _prepare_data(data: list[tuple]) -> dict:
    prepare_data = {}
    for elem in data:
        name = elem[0]
        hours = int(elem[1])
        if name in prepare_data:
            prepare_data[name]['hours'].append(hours)
            prepare_data[name]['sum_hours'] = sum(prepare_data[name]['hours'])
        else:
            prepare_data[name] = {'hours': [hours]}
    return prepare_data


def print_data(result_data: list[Data]) -> None:
    for data in result_data:
        hours = [str(h) for h in data.hours]
        print(f'{data.name}: {", ".join(hours)}, sum: {data.sum_hours}')


def run():
    data = write_file('data.txt')
    res = get_statistic(data)
    print_data(res)


if __name__ == '__main__':
    run()
