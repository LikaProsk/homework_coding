import itertools
import re
import subprocess
import pendulum

from operator import itemgetter


class SystemProcessParser:

    def __get_system_process(self):
        return subprocess.check_output(['ps', 'aux'], universal_newlines=True, stderr=subprocess.STDOUT)

    def parse(self):
        sys_proc = self.__get_system_process()
        if len(sys_proc) > 0:
            proc_by_lines = sys_proc.split('\n')
            if 'PID' in proc_by_lines[0]:
                result = []
                columns = re.split(r'\s+', proc_by_lines[0])
                proc_by_lines.pop(0)
                for row in proc_by_lines:
                    if row == '':
                        continue

                    row = re.split(r'(.*\d+:\d{2}.\d{2})', row)
                    columns_value = re.split(r'\s+', row[1]) + [row[2]]
                    if len(columns) == len(columns_value):
                        result.append({columns[i]: columns_value[i] for i in range(0, len(columns))})
                    else:
                        raise 'Количество значений не соответствует количеству столбцов'

                return result

    def generate_report(self):
        process_info = self.parse()
        sys_users = self.__get_sys_user(process_info)
        count_proc_by_user = '  \n'.join(self.__get_user_count_pocess(process_info))
        if len(process_info):
            report = 'Отчёт о состоянии системы:\n' \
                     f'Пользователи системы:{", ".join(sys_users)}\n' \
                     f'Процессов запущено: {len(process_info)}\n' \
                     f'Пользовательских процессов:\n{count_proc_by_user}\n' \
                     f'Всего памяти используется: {round(self.__get_memory_total(process_info), 2)} Mb\n' \
                     f'Всего CPU используется: {round(self.__get_cpu_total(process_info), 2)} %\n' \
                     f'Больше всего памяти использует: {self.__get_proc_max_resources_used(process_info, "RSS")}\n' \
                     f'Больше всего CPU использует: {self.__get_proc_max_resources_used(process_info, "%CPU")}\n'

            print(report)
            self.__save_report(report)
        else:
            raise 'Неудалось получить информацию о системных процессах'

        return report

    def __get_sys_user(self, process_info):
        return set([column.get('USER') for column in process_info])

    def __get_user_count_pocess(self, process_info):
        sorted_user = sorted(process_info, key=itemgetter('USER'))
        return [f'  {key}: {len([item for item in group])}'
                for key, group in itertools.groupby(sorted_user, lambda item: item.get('USER'))]

    def __get_memory_total(self, process_info):
        return sum([int(row.get('RSS')) for row in process_info]) * 0.001024

    def __get_cpu_total(self, process_info):
        return sum([float(row.get('%CPU')) for row in process_info])

    def __get_proc_max_resources_used(self, process_info, resources):
        max_used = max(process_info, key=lambda row: float(row.get(resources)))
        result = 'Процесс не найден'
        if 'COMMAND' in max_used:
            result = f'{max_used.get("COMMAND")[:20]}...' if len(max_used.get('COMMAND')) > 20 else max_used.get(
                'COMMAND')
        return result

    def __save_report(self, report):
        name = f'{pendulum.now("UTC").strftime("%d-%m-%Y-%H:%M")}-scan.txt'
        with open(name, 'w') as outfile:
            outfile.write(report)


if __name__ == "__main__":
    SystemProcessParser().generate_report()
