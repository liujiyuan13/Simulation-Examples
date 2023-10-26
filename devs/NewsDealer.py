import Rand

news_day_type = [0,1,2] # Good, Fair, Poor
news_day_type_prob = [0.35,0.45,0.20]

good_demand = [40,50,60,70,80,90,100]
good_prob = [0.03,0.05,0.15,0.20,0.35,0.15,0.07]
fair_demand = [40,50,60,70,80,90,100]
fair_prob = [0.10,0.18,0.40,0.20,0.08,0.04,0.00]
poor_demand = [40,50,60,70,80,90,100]
poor_prob = [0.44,0.22,0.16,0.12,0.06,0.00,0.00]

demands = [[good_demand,good_prob],[fair_demand,fair_prob],[poor_demand,poor_prob]]
one_paper_order = 0.33
one_paper_sales = 0.5
one_paper_lost_profit_from_excess_demand = 0.17
one_paper_salvage = 0.05

order_papers = 70

def DayProfit():
    type = Rand.uniformDiscrete(news_day_type,news_day_type_prob,3)
#    print(demands[type])
    demand = Rand.uniformDiscrete(demands[type][0],demands[type][1],7)
    profit = 0
    if(demand > order_papers):
        profit = order_papers * one_paper_sales - order_papers * one_paper_order 
        - (demand - order_papers) * one_paper_lost_profit_from_excess_demand
    else:
        profit = demand  * one_paper_sales - order_papers * one_paper_order 
        + (order_papers - demand) * one_paper_salvage
#    print(order_papers)  
#    print(type)     
#    print(demand)     
#    print(profit)        
    return profit

def MonthProfit():
    clock = 1
    profits = 0
    dayProfits = []
    for i in range(20):
        clock += 1
        profit = DayProfit()
        dayProfits.append(profit)
        profits += profit
    return [dayProfits,profits]

