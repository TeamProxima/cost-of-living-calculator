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
    breakfast_total = 0
    lunch_total = 0
    dinner_total = 0

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
            breakfast_total += in_ratio * breakfast_at_home + (1 - in_ratio) * breakfast_at_outside
        elif meal == "Lunch":
            lunch_total += in_ratio * lunch_at_home + (1 - in_ratio) * lunch_at_outside
        elif meal == "Dinner":
            dinner_total += in_ratio * dinner_at_home + (1 - in_ratio) * dinner_at_outside

    total += breakfast_total + lunch_total + dinner_total
    fruit_cost = (apple + banana + orange) * 0.1
    total += fruit_cost


    return {'Breakfast':breakfast_total*30,'Lunch':lunch_total*30,'Dinner':dinner_total*30, 'Fruit':fruit_cost*30 , 'Total':total*30}

def beer_cigarette_cost(beer_count,cigarette_count, prices):
    d_beer_res = prices[3]
    i_beer_res = prices[4]

    d_beer_market = prices[24]
    i_beer_market = prices[25]

    cigarette = prices[26]

    beer_total = ((d_beer_market + d_beer_res + (i_beer_market + i_beer_res)*5/3.3)/4)*beer_count/7
    cig_total = cigarette*cigarette_count/7

    total = beer_total + cig_total

    return {'Beer':beer_total*30,'Cigarette':cig_total*30, 'Total': total*30}

def accomodation_cost36(location,bedroom_count,prices):
	in_city_centre_1bedroom = prices[44]
	in_city_centre_3bedrooms = prices[46]
	in_city_centre_2bedrooms = (in_city_centre_3bedrooms + in_city_centre_1bedroom)/2
	outside_city_centre_1bedroom = prices[45]
	outside_city_centre_3bedrooms = prices[47]
	outside_city_centre_2bedrooms = (outside_city_centre_3bedrooms + outside_city_centre_1bedroom)/2

	total = 0;

	if location == "In city centre":
		if bedroom_count == 1:
			return in_city_centre_1bedroom
		elif bedroom_count == 2:
			return in_city_centre_2bedrooms
		else:
			return in_city_centre_3bedrooms
	else:
		if bedroom_count == 1:
			return outside_city_centre_1bedroom
		elif bedroom_count == 2:
			return outside_city_centre_2bedrooms
		else:
			return outside_city_centre_3bedrooms

def utilities_cost36(bedroom_count,prices):
	basic_cost = prices[34]
	internet_cost = prices[36]
	total = 0

	total += internet_cost

	if bedroom_count == "1":
		total += basic_cost
	else:
		total += basic_cost*1.7

	return total

def misc_cost36(clothes_count, cinema_count, fitness, prices):
	clothes_cost = (prices[40] + prices[41] + prices[42] + prices[43])/4
	cinema_cost = prices[39]
	fitness_cost = prices[37]
	total = 0;

	clothes_total = clothes_cost*clothes_count/30.0
	cinema_total = cinema_cost*cinema_count/30.0
	fitness_total = 0
	if fitness == "Yes":
		fitness_total = fitness_cost/30.0
	total = clothes_total + cinema_total + fitness_total

	return {'Outfit': clothes_total*30, 'Cinema': cinema_total*30, 'Fitness':fitness_total*30, 'Total':total*30}

def transportation_cost36(drive_miles, public_trans_count, taxi_count, uber_base, uber_km, prices):
	oneway_ticket = prices[27]
	monthly_ticket = prices[28]
	taxi_start_cost = prices[29]
	taxi_km_cost = prices[30]
	gasoline_cost = prices[32]

	total = 0;

	cab_cost = (taxi_start_cost + taxi_km_cost*7)*taxi_count/7.0
	uber_cost = (uber_base + uber_km*7)*taxi_count/7.0
	if uber_base == -1:
		taxi_cost = cab_cost
	else:
		taxi_cost = (cab_cost + uber_cost)/2.0

	public_trans_cost = 0
	if public_trans_count > 15:
		public_trans_cost = monthly_ticket/30.0
	else:
		public_trans_cost = public_trans_count*oneway_ticket/7

	drive_kilometers = drive_miles*1.60934
	liter_consumed = drive_kilometers/9.9
	drive_cost = liter_consumed*gasoline_cost/7

	total = public_trans_cost + taxi_cost + drive_cost
	return {'Public_Trans':public_trans_cost*30,'Taxi_Total':taxi_cost*30,'Drive_Total':drive_cost*30, 'Uber':uber_cost*30, 'Cab':cab_cost*30, 'Total':total*30}