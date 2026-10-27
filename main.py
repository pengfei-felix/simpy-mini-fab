import simpy
import random

# 工程引用
from fab.model import FLOW_LIST
from fab.workorder import WorkOrder


# 定义Fab类：仿真主体
class Fab:
    def __init__(self, work_order):
        self.env = simpy.Environment()
        self.work_order = work_order

        # 初始化机台池
        self.eqp_tool = self.eqp_tool_init()
        pass

    # 初始化机台池
    def eqp_tool_init(self):

        # 定义机台池
        # 机台名：这里的机台名要和产品中的工艺需要要对应。*注意*
        # capacity：机台同时加工Lot数量。
        eqp_tool = {
            "LITHO": simpy.Resource(self.env, capacity=1),
            "ETCH": simpy.Resource(self.env, capacity=2),
            "WET": simpy.Resource(self.env, capacity=4),
            "DIFF": simpy.Resource(self.env, capacity=4)
        }
        return eqp_tool

    # 工艺加工：模拟lot在机台上进行加工，支持Flow。
    def eqp_process(self, lot_id, product):
        for i, (eqp_type, eqp_pt) in enumerate(product, 1):
            print(f"t = {self.env.now}, lot{lot_id} arrive {eqp_type} step.")
            with self.eqp_tool[eqp_type].request() as rq:
                yield rq 
                print(f"t = {self.env.now}, lot{lot_id} jobin on {eqp_type}.")
                yield self.env.timeout(eqp_pt)
            print(f"t = {self.env.now}, lot{lot_id} jobout.") 
        print(f"t = {self.env.now}, all lot{lot_id} finish.") 



    # 定义下线函数：投放Lot
    def wafer_start(self, work_order):

        # lot_cnt = sum(work_order.product_list[1::2])
        product_list = work_order.product_list
        lot_id = 1


        # 循环下线
        print(f"-------------下线工单-------------")
        print(f"1. Product List: {work_order.product_list}")
        print(f"2. Lot Qty: {work_order.lot_cnt}")
        print(f"---------------------------------")
        for product, cnt in work_order.product_list:
            for n in range(cnt):
                # 每隔1个仿真时间，下线1个lot。
                yield self.env.timeout(1) 
                self.env.process(self.eqp_process(lot_id, FLOW_LIST[product]))
                lot_id += 1
        print(f"-------------下线完成-------------")


    def run(self):
        # 开始下线
        self.env.process(self.wafer_start(self.work_order))
        # 仿真开始
        self.env.run()


if __name__ == "__main__":

    product_list = [("PRODUCT_A", 0.5), ("PRODUCT_B", 0.5)]
    lot_cnt = 10
    work_order = WorkOrder("normal", lot_cnt, product_list)

    mini_fab = Fab(work_order)
    mini_fab.run()