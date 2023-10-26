def function1(functionaux, list):

    results = []
    
    for element in list:
        result = functionaux(element)
        results.append(result)
    return results