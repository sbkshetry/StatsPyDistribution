from src.NormalDistribution import NormalDistribution as ND

n = ND(1, 4)
n.plot()
n.plot(y=n.cumulative_distribution_function_value())
n.plot(y=n.movement_generating_function_value())