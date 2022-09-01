import sys
import json
import time
from datetime import datetime

class GoodsTaskHandler(object):
    def __init__(self, param):
        self.param_dict = self.get_param_dict(param)
        print('param_dict: ', self.param_dict)

    @staticmethod
    def get_param_dict(param):
        param_dict = {}
        try:
            param_dict = json.loads(param)
        except Exception as e:
            print(e)
        return param_dict

    def demo(self):
        print("start: ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        time.sleep(100)
        print("end: ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def main():
    print('sys.argv: ', sys.argv)
    func_name = sys.argv[1]
    print('function_name: ', func_name)
    try:
        param = sys.argv[2]
    except Exception as e:
        print(e)
        param = ''
    print('param: ', param)
    goods_task_handler = GoodsTaskHandler(param)
    print(hasattr(goods_task_handler, func_name))
    if hasattr(goods_task_handler, func_name):
        func = getattr(goods_task_handler, func_name)
        print('func: ', func)
        func()
