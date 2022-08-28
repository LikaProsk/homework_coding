import logging
import os
import sys
import uuid

import pendulum as pendulum


class LoggingHelper:
    def __init__(self, root_dir, test_name):
        super().__init__()
        self.logger = None
        self.root_dir = root_dir
        self.session_id = str(uuid.uuid4())
        self.path_artifacts_test = self._path_artifacts_test(self.root_dir, test_name, self.session_id)
        self.log_file = self.path_log_file()

    @staticmethod
    def __get_time(time_format: str):
        return pendulum.now('UTC').strftime(time_format)

    def _path_artifacts_test(self, root_dir: str, test_name: str, session_id: str):
        return os.path.join(root_dir, 'logs', self.__get_time('%d-%m-%Y %H') + '-' + test_name + ' - ' + session_id)

    def log(self):
        if self.logger is None:
            self.logger = logging.getLogger(self.session_id)
            if not self.logger.handlers:
                self.logger.setLevel(logging.DEBUG)
                fh = logging.FileHandler(self.log_file, 'w', 'utf-8')
                formatter = logging.Formatter('%(asctime)s - %(name)s -  %(module)s - %(levelname)s - %(message)s')
                fh.setFormatter(formatter)
                self.logger.addHandler(fh)
                sh = logging.StreamHandler(sys.stderr)
                sh.setFormatter(formatter)
                self.logger.addHandler(sh)
        return self.logger

    def path_log_file(self):
        log_console_path = self.path_artifacts_test
        if not os.path.exists(log_console_path):
            os.makedirs(log_console_path)
        date = self.__get_time('%d-%m-%Y %H-%M-%S-%f')
        return os.path.join(log_console_path, date + '.log')
