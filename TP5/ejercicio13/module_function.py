import math

def module_calculator(vector_parameters):
    addition = sum(parameter ** 2 for parameter in vector_parameters)
    module = math.sqrt(addition)
    return module