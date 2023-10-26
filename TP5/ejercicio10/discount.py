def discount_calculator(product_dict):
    final_price = 0
    for product, discount in product_dict.items():
        final_price += product - (product*(discount/100))
    
    return final_price