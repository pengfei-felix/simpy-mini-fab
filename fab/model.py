# Mini Fab仿真
# 产品FLow
# 描述：主要是定义各个产品的Flow，即Lot需要加工的机台是顺序。

# 键值对：工艺区域 : PT（加工时间）
# 工艺区域: Lot加工的工艺区域，这里需要和机台名相同，便于和机台进行Mapping。
# PT: 机台加工的时间，这里指仿真时间。
PRODUCT_A = [
    ("LITHO", 10),
    ("ETCH", 5)
]

PRODUCT_B = [
    ("WET", 5),
    ("DIFF", 20)
]

PRODUCT_C = [
    ("WET", 5),
    ("DIFF", 20),
    ("LITHO", 10),
    ("ETCH", 5)
]
PRODUCT_LIST = ["PRODUCT_A", "PRODUCT_B", "PRODUCT_C"]
FLOW_LIST = {
    "PRODUCT_A" : PRODUCT_A,
    "PRODUCT_B" : PRODUCT_B, 
    "PRODUCT_C" : PRODUCT_C
}