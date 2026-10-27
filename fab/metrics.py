# Mini Fab仿真
# 工单

class WorkOrder:
    def __init__(self, mode,lot_cnt, products=None):

        # 校验入参合法
        self._validate(mode, lot_cnt, products)

        self.mode = mode
        self.lot_cnt = lot_cnt
        self.product_list = self._set_product_list(mode, lot_cnt, products)
        

    def _validate(self, mode, lot_cnt, products):

        if lot_cnt == 0:
            raise ValueError(f"投料数量必须大于0")
        if mode not in ("random", "normal"):
            raise ValueError(f"不支持的投料模式: {mode}")
        if mode == "normal" and products is None:
            raise ValueError(f"normal模式必须指定product和投放比例")

    def _set_product_list(self, mode, lot_cnt, products):
        if mode == "random":
            product = random.choice(PRODUCT_LIST)
            return [(product, lot_cnt)]

        # Normal模式投料
        elif mode == "normal":

            # 单一产品投料
            if len(products) == 1:
                return [products[0][0], lot_cnt]

            # 混合多种产品投料
            result = []
            remaing_lot_cnt = lot_cnt
            for product, ratio in products[:-1]:
                n = int(lot_cnt * ratio)
                result.extend((product, n))
                remaing_lot_cnt = remaing_lot_cnt - n 
            last_product = products[-1][0]
            result.extend((last_product, remaing_lot_cnt))
            return result