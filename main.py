import simpy

## 定义产品Flow

PRODUCT_A = [
    ("LITHO", 10),
    ("ETCH", 5)
]

# 定义Fab类：仿真主体
class Fab:
    def __init__(self):
        self.eqp_tool = self.eqp_tool_init()
        pass

    # 初始化机台池
    def eqp_tool_init(self):
        eqp_tool = {
            "LITHO": simpy.Resource(env, capacity=1),
            "ETCH": simpy.Resource(env, capacity=2)
        }
        return eqp_tool

    # 工艺加工：模拟lot在机台上进行加工，支持Flow。
    def eqp_process(self, env, lot_id, product):
        for i, (eqp_type, eqp_pt) in enumerate(product, 1):
            print(f"t = {env.now}, lot{lot_id} arrive.")
            with self.eqp_tool[eqp_type].request() as rq:
                yield rq 
                print(f"t = {env.now}, lot{lot_id} jobin on {eqp_type}.")
                yield env.timeout(eqp_pt)
            print(f"t = {env.now}, lot{lot_id} jobout.") 
        print(f"t = {env.now}, lot{lot_id} finish.") 


        


# 定义下线函数：投放Lot
def wafer_start(env, fab, lot_cnt):
    global PRODUCT_A
    for i in range(lot_cnt):
        yield env.timeout(1)
        lot_id = i 
        env.process(fab.eqp_process(env, lot_id, PRODUCT_A))

if __name__ == "__main__":

    env = simpy.Environment()
    fab = Fab()
    env.process(wafer_start(env, fab, 2))
    env.run()
