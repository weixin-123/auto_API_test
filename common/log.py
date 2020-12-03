import os
import logging
from datetime import datetime
import threading


class Log:

    # 这边需要传一个测试用例名称
    def __init__(self, test_case_name):
        global logPath, resultPath, pro_dir
        pro_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        resultPath = os.path.join(pro_dir, "result", "log")
        logPath = os.path.join(pro_dir, "result", "log")

        resultPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d")))

        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        # logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        # if not os.path.exists(logPath):
        #     os.mkdir(logPath)

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        # defined handler
        test_case_name = os.path.split(test_case_name)[-1].split(".")[0]
        handler = logging.FileHandler(os.path.join(resultPath, test_case_name + "_" + str(datetime.now().strftime("%Y%m%d%H%M%S")) + ".log"))
        # defined formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def get_logger(self):
        """
        get logger
        :return:
        """
        return self.logger

    def build_start_line(self, case_no):
        """
        write start line
        :return:
        """
        self.logger.info("--------" + case_no + " START--------")

    def build_end_line(self, case_no):
        """
        write end line
        :return:
        """
        self.logger.info("--------" + case_no + " END--------")

    def build_case_line(self, case_name, code, msg):
        """
        write test case line
        :param case_name:
        :param code:
        :param msg:
        :return:
        """
        self.logger.info(case_name+" - Code:"+code+" - msg:"+msg)

    def get_report_path(self):
        """
        get report file path
        :return:
        """
        report_path = os.path.join(logPath, str(datetime.now().strftime("%Y%m%d%H%M%S")) + ".html")
        return report_path

    def get_result_path(self):
        """
        get test result path
        :return:
        """
        return logPath

    def write_result(self, result):
        """

        :param result:
        :return:
        """
        result_path = os.path.join(logPath, "report.txt")
        fb = open(result_path, "wb")
        try:
            fb.write(result)
        except FileNotFoundError as ex:
            logger.error(str(ex))


class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():

        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()

        return MyLog.log


if __name__ == "__main__":
    log = Log(test_case_name="test_goods_detail_")
    logger = log.get_logger()
    a = r"C:\Users\Administrator\PycharmProjects\shall_buy_test\test_case\goods_service\goods\test.py"
    print(os.path.split(a)[-1].split(".")[0])
    logger.debug("test debug")
    logger.info("test info")

