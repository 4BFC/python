def make_change(coins, amount):
    coins.sort(reverse=True)
    print(coins)  # 25,10,5,1
    # reverse = True이면 오름차순이다.
    # coins의 정렬을 오름차순으로 진행 한다.
    change = []
    for coin in coins:
        while amount >= coin:  # amount가 coin보다 같거나 크다면
            change.append(coin)
            print(change)  #
            # 해당 코인을 리스트에 추가하고 제외(뺄셈)하고 남은 amount에서 값을 다시 돌린다. 이때 while문의 조건인 amount보다 coin이 클경우 특정 코인 종류에서 계속해서 특정 코인의 값이 차감된다. 이후 amount가 특정 코인 보다 작아지면 그 다음 코인의 종류로 넘어가 위와 같은 방법으로 다시 수행한다.
            amount -= coin
    return change


# 동전 종류와 지불할 금액
coin_list = [25, 10, 5, 1]
amount_to_pay = 63

# 그리디 알고리즘을 사용하여 거스름돈 계산
change = make_change(coin_list, amount_to_pay)

# 결과 출력
print("지불할 금액:", amount_to_pay)  # 63
print("거스름돈:", change)  # 41
