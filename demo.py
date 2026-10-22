import simpy

cycle_cnt = 1

def study_rest_cycle(env):
    global cycle_cnt
    while True:
        print(f"------Cycle {cycle_cnt}------")
        print(f"{env.now}s 开始专注学习")
        yield env.timeout(30)

        print(f"{env.now}s 学习结束，开始休息")
        cycle_cnt = cycle_cnt + 1
        yield env.timeout(10)

env = simpy.Environment()
env.process(study_rest_cycle(env))
env.run(until=120)