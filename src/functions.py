def meal_cost(meal_types, veg_ratio, out_meal_count, restaurant_ratio, prices):
    """
    meal_types: string array containing some of "Breakfast", "Lunch" and "Dinner"
    veg_ratio: ratio of eating vegatables
    in_ratio: ratio of eating at house
    restaurant_ratio: ratio of eating at restaurant
    """

    inexp_rest = prices[0]
    fastfood_rest = prices[2]
    coke = prices[6]
    milk = prices[8]
    bread = prices[9]
    rice = prices[10]
    egg = prices[11]
    cheese = prices[12]
    chicken = prices[13]
    beef = prices[14]
    apple = prices[15]
    banana = prices[16]
    orange = prices[17]
    tomato = prices[18]
    potato = prices[19]
    onion = prices[20]
    lettuce = prices[21]
    water = prices[22]
    
    total = 0
    
    in_ratio = (len(meal_types)*7 - out_meal_count)/(len(meal_types)*7)

    breakfast_at_home = milk / 4 + bread / 5 + egg / 12 + cheese / 20 + water / 3
    breakfast_at_outside = breakfast_at_home * 2

    if veg_ratio < 50:
        dinner_at_home = bread / 5 + rice / 10 + (1-veg_ratio)*(chicken + beef) / 12 + veg_ratio*(tomato + potato + onion + lettuce) / 20 + water
    else:
        dinner_at_home = bread / 5 + rice / 10 + (1-veg_ratio)*(chicken + beef) / 12 + 4*veg_ratio*(tomato + potato + onion + lettuce) / 20 + water

    dinner_at_outside = (inexp_rest + coke) * restaurant_ratio + fastfood_rest * (1 - restaurant_ratio)

    lunch_at_home = dinner_at_home * 0.8
    lunch_at_outside = dinner_at_outside * 0.8

    for meal in meal_types:
        if meal == "Breakfast":
            total += in_ratio * breakfast_at_home + (1 - in_ratio) * breakfast_at_outside
        elif meal == "Lunch":
            total += in_ratio * lunch_at_home + (1 - in_ratio) * lunch_at_outside
        elif meal == "Dinner":
            total += in_ratio * dinner_at_home + (1 - in_ratio) * dinner_at_outside

    fruit_cost = (apple + banana + orange) * 0.1
    total += fruit_cost

    return total

def beer_cigarette_cost(beer_count,cigarette_count, prices):
    d_beer_res = prices[3]
    i_beer_res = prices[4]
    d_beer_market = prices[24]
    i_beer_market = prices[25]
    cigarette = prices[26]

    total = ((d_beer_market + d_beer_res + (i_beer_market + i_beer_res)*5/3.3)/4)*beer_count/7
    total += cigarette*cigarette_count/7

    return total

#print meal_cost(["Breakfast","Lunch","Dinner"], 0.7, 0.3, 0.7)
#print beer_cigarette_cost(1,4)