annual_basketball_fee = int(input())

calc_for_basketball_sneakers = annual_basketball_fee * 0.40
basketball_sneakers = annual_basketball_fee - calc_for_basketball_sneakers

calc_for_basketball_outfit = basketball_sneakers * 0.20
basketball_outfit = basketball_sneakers - calc_for_basketball_outfit

basket_ball = basketball_outfit * 0.25

basketball_accessories = basket_ball * 0.20

final_price = annual_basketball_fee + basketball_sneakers + basketball_outfit + basket_ball + basketball_accessories

print(final_price)
