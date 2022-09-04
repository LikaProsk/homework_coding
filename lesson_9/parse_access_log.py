import itertools
import json
import os
import re
import subprocess
from operator import itemgetter
from optparse import OptionParser


class ParseAccessLog:

    def add_option(self):
        parser = OptionParser()
        parser.add_option("--dir_path", action="store", default=None, help="Путь до папки с access логами")
        parser.add_option("--file_path", action="store", default=None, help="Путь к файлу с access логами")
        (options, args) = parser.parse_args()
        return options

    def loading_assess_log(self, dir_path=None, file_path=None):
        if dir_path is not None:
            logs_path = self.__find_acess_log_by_dir(dir_path)
        elif file_path is not None:
            if os.path.isfile(file_path) and 'access' in file_path:
                logs_path = [file_path]
            else:
                raise FileExistsError(f'Не удалось найти файл access лога по пути {file_path}')
        else:
            raise ValueError('Необходимо указать путь до папки или путь до файла с access логом')

        context = self.__get_context(logs_path)

        return context

    def __get_context(self, logs_path):
        context = []
        for log_path in logs_path:
            if log_path == '':
                continue
            with open(log_path, 'r') as f:
                context += f.readlines()

        result = []
        for row in context:
            pars_row = re.search(
                r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(.*)\] '
                r'"(GET|POST|PUT|PATH|DELETE|HEAD|OPTIONS|CONNECT|TRACE) (.*)'
                r'(HTTP\/\d.\d)" (\d{1,3}) (\d+) "(\W+)" "(.*)" (\d+)', row)
            if pars_row is None:
                continue

            result.append({
                'ip': pars_row.groups()[0],
                'date_and_time': pars_row.groups()[1],
                'method': pars_row.groups()[2],
                'uri': pars_row.groups()[3],
                'http_version': pars_row.groups()[4],
                'status_code': pars_row.groups()[5],
                'count_bytes_return': pars_row.groups()[6],
                'referer': pars_row.groups()[7],
                'user_agent': pars_row.groups()[8],
                'response_time': pars_row.groups()[9]
            })

        return result

    def generate_report(self, context):
        if not len(context):
            raise Exception('Access лог пуст')

        requests_total = len(context)
        http_count_methods = self.__get_http_count_methods(context)
        top_3_ip_max_query = self.__get_top_3_ip_max_query(context)
        top_3_long_queries = self.__get_top_3_long_queries(context)

        self.__save_in_json(http_count_methods, requests_total, top_3_ip_max_query, top_3_long_queries)
        self.__print_reports(http_count_methods, requests_total, top_3_ip_max_query, top_3_long_queries)

    def __save_in_json(self, http_count_methods, requests_total, top_3_ip_max_query, top_3_long_queries):
        report = {
            'report':
                {
                    'requests_total': requests_total,
                    'http_count_methods': http_count_methods,
                    'top_3_ip_max_query': top_3_ip_max_query,
                    'top_3_long_queries': top_3_long_queries
                }
        }

        with open('report.json', 'w') as f:
            f.write(json.dumps(report))

    def __find_acess_log_by_dir(self, dir_path):
        if os.path.isdir(dir_path):
            result = subprocess.check_output(
                ['find', f'{dir_path}', '-name', '*access*.log'],
                universal_newlines=True,
                stderr=subprocess.STDOUT)
            if result != '':
                return result.split('\n')
            else:
                raise FileExistsError(f'Не удалось найти access.log в папке {dir_path}')
        else:
            raise OSError(f'Папка "{dir_path}" не найдена')

    def __get_http_count_methods(self, context):
        sorted_by_method = sorted(context, key=itemgetter('method'))
        return {key: len([item for item in group])
                for key, group in itertools.groupby(sorted_by_method, lambda item: item.get('method'))}

    def __get_top_3_ip_max_query(self, context):
        sorted_by_ip = sorted(context, key=itemgetter('ip'))
        result = {key: len([item for item in group])
                  for key, group in itertools.groupby(sorted_by_ip, lambda item: item.get('ip'))}
        return sorted(result, key=lambda item: item[1], reverse=True)[:3]

    def __get_top_3_long_queries(self, context):
        sorted_by_rt = sorted(context, key=itemgetter('response_time'), reverse=True)[:3]
        return [{
            'method': item.get('method'),
            'uri': item.get('uri'),
            'ip': item.get('method'),
            'response_time': item.get('response_time'),
            'date_and_time': item.get('date_and_time')
        } for item in sorted_by_rt]

    def __print_reports(self, http_count_methods, requests_total, top_3_ip_max_query, top_3_long_queries):
        http_count_methods_str = '\n    '.join(http_count_methods)
        top_3_ip_max_query_str = '\n    '.join([str(i) for i in top_3_ip_max_query])
        top_3_long_queries_str = '\n    '.join([str(i) for i in top_3_long_queries])

        report = f'Общее количество выполненных запросов: {requests_total}\n' \
                 f'Количество запросов по HTTP-методам:\n   {http_count_methods_str}\n' \
                 f'Топ 3 IP адресов, с которых были сделаны запросы:\n  {top_3_ip_max_query_str}\n' \
                 f'Tоп 3 самых долгих запросов:\n   {top_3_long_queries_str}'

        print(report)


if __name__ == '__main__':
    parsr_log = ParseAccessLog()
    options = parsr_log.add_option()
    context = parsr_log.loading_assess_log(dir_path=options.dir_path, file_path=options.file_path)
    parsr_log.generate_report(context)
