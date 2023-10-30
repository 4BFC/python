def activity_selection(activities):
    activities.sort(key=lambda x: x[1])  # 종료 시간을 기준으로 정렬
    #lambda함수를 아직 모른다. 
    selected_activities = [activities[0]]
    last_activity = activities[0]

    for activity in activities[1:]:
        start, end = activity
        last_end = last_activity[1]
        if start >= last_end:
            selected_activities.append(activity)
            last_activity = activity

    return selected_activities

# 활동 목록 [시작 시간, 종료 시간]
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]

# 그리디 알고리즘을 사용하여 활동 선택
selected = activity_selection(activities)

# 결과 출력
print("선택된 활동:", selected)
