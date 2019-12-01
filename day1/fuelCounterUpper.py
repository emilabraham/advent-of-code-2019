import math

#List of masses for the modules
masses = [70102,
        60688,
        105331,
        127196,
        141253,
        118164,
        67481,
        75634,
        60715,
        84116,
        51389,
        52440,
        84992,
        87519,
        85765,
        124479,
        97873,
        85437,
        94902,
        124969,
        70561,
        144601,
        128042,
        67596,
        136905,
        111849,
        100389,
        135608,
        91006,
        77385,
        52100,
        64728,
        127796,
        114893,
        82414,
        66565,
        73704,
        110396,
        142722,
        107813,
        149628,
        131729,
        118421,
        56566,
        84962,
        108120,
        108438,
        81536,
        55238,
        77072,
        132575,
82716,
50641,
57320,
        89661,
        97094,
        134713,
        142451,
128541,
53527,
116088,
101909,
124349,
103812,
108324,
72981,
114488,
78738,
78523,
129146,
103007,
68506,
102227,
93507,
94557,
105867,
125514,
109130,
146102,
100876,
143549,
85753,
97589,
90892,
104287,
70930,
53847,
94687,
135370,
76024,
76156,
101006,
128349,
58134,
110849,
149176,
136728,
79054,
136740,
131081]

#Return fuel required to launch a module given its mass
def fuelCalc(mass):
    return math.floor(mass/3) - 2

#Return the sum of fuel needed for each module
def fuelSum():
    fuelSum = 0

    for f in masses:
        fuelSum += fuelCalc(f)

    return fuelSum

#Return the cumulative sum of fuel needed for a given module
def fuelCumCalc(mass, acc):
    fuelAddition = fuelCalc(mass)
    if fuelAddition >= 0:
        acc += fuelAddition
    if fuelAddition <= 0:
        return acc
    else:
        return fuelCumCalc(fuelAddition, acc)

#Return the sum of cumulative sum of fuel for each module
def fuelCumSum():
    fuelCumSum = 0

    for f in masses:
        fuelCumSum += fuelCumCalc(f, 0)

    return fuelCumSum

print(fuelCalc(12))
print(fuelCalc(14))
print(fuelCalc(1969))
print(fuelCalc(100756))
print(fuelSum())

print(fuelCumCalc(14, 0))
print(fuelCumCalc(1969, 0))
print(fuelCumCalc(100756, 0))
print(fuelCumSum())
