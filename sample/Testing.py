from src.NormalDistribution import NormalDistribution as ND
from src.ExponentialDistribution import ExponentialDistribution as ED
from src.RectangularDistribution import RectangularDistribution as RD
from src.TriangularDistribution import TriangularDistribution as TD
from src.SymmetricTriangularDistribution import SymmetricTriangularDistribution as STD
from src.BinomialDistribution import BinomialDistribution as BD
from src.PoissonDistribution import PoissonDistribution as PD
from src.GeometricDistribution import GeometricDistribution as GD
from src.HypergeometricDistribution import HypergeometricDistribution as HGD
from matplotlib import pyplot as plt

# NormalDistribution
d = ND(0.0, 4, size=100)
d_data = d.data()

d1 = ND(0.0, 2.5, size=100)
d_data1 = d1.data()

d2 = ND(-5.0, 5, size=100)
d_data2 = d2.data()

d3 = ND(2.0, 8, size=100)
d_data3 = d3.data()
# ExponentialDistribution
"""
d = ED(0.5)
d_data = d.data()

d1 = ED(1.0)
d_data1 = d1.data()

d2 = ED(1.5)
d_data2 = d2.data()

d3 = ED(2.0)
d_data3 = d3.data()
"""
# RectangularDistribution
"""
d = RD(0.0, 2)
d_data = d.data()

d1 = RD(0.0, 5)
d_data1 = d1.data()

d2 = RD(-5.0, 5)
d_data2 = d2.data()

d3 = RD(2.0, 10)
d_data3 = d3.data()
"""

# TriangularDistribution
"""
d = TD(0.0, 2)
d_data = d.data()

d1 = TD(0.0, 5)
d_data1 = d1.data()

d2 = TD(-5.0, 5)
d_data2 = d2.data()

d3 = TD(2.0, 10)
d_data3 = d3.data()
"""
# SymmetricTriangularDistribution
"""
d = STD(0.0, 2)
d_data = d.data()

d1 = STD(0.0, 5)
d_data1 = d1.data()

d2 = STD(-5.0, 5)
d_data2 = d2.data()

d3 = STD(2.0, 10)
d_data3 = d3.data()
"""

# BinomialDistribution
"""
d = BD(0.2, size=20)
d_data = d.data()
d1 = BD(0.5, size=20)
d_data1 = d1.data()
d2 = BD(0.7, size=20)
d_data2 = d2.data()
d3 = BD(0.5, size=40)
d_data3 = d3.data()
"""
# PoissonDistribution
"""
d = PD(1)
d_data = d.data()
d1 = PD(4)
d_data1 = d1.data()
d2 = PD(8)
d_data2 = d2.data()
d3 = PD(10)
d_data3 = d3.data()
"""
# GeometricDistribution
"""
d = GD(0.2)
d_data = d.data()
d1 = GD(0.5)
d_data1 = d1.data()
d2 = GD(0.8)
d_data2 = d2.data()
d3 = GD(0.9)
d_data3 = d3.data()
"""
# HypergeometricDistribution
"""
d = HGD(500, 50, 100)
d_data = d.data()
d1 = HGD(500, 60, 200)
d_data1 = d1.data()
d2 = HGD(500, 70, 300)
d_data2 = d2.data()
d3 = HGD(500, 80, 300)
d_data3 = d3.data()
"""
list = [(d_data, d), (d_data1, d1), (d_data2, d2), (d_data3, d3)]

diplay = "fx"

for l in list:
    x = l[0]['x']
    y = l[0]['y']
    d = l[1]
    if diplay == "cfx":
        y = d.cumulative_distribution_function_value()
    plt.scatter(x, y, s=2.0, label=d.__str__())
    plt.plot(x, y)

    # plt.axvline(d.kurtosis(), color='r', linestyle='--', label=f'kurtosis: {d.kurtosis()}')
    # plt.axvline(d.skewness(), color='g', linestyle='--', label=f'skewness: {d.skewness()}')
    # plt.axvline(d.mean(), color='r', linestyle='-.', label=f'mean: {d.mean()}')
    # plt.axvline(d.variance(), color='g', linestyle='-.', label=f'variance: {d.variance()}')

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title(d.name())
plt.legend()
plt.show()
