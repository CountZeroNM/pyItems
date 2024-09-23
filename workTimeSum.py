def sum_times(times_list):
    total_minutes = 0
    for time in times_list:
        hours, minutes = map(int, time.split(':'))
        total_minutes += hours * 60 + minutes
    
    # 合計時間を計算
    total_hours = total_minutes // 60
    remaining_minutes = total_minutes % 60

    return f"{total_hours}:{remaining_minutes:02d}"

# ユーザー入力
input_times = input("時間をカンマ区切りで入力してください(例: 10:45, 9:10, 6:45): ")

# カンマで区切ってリストに変換
times_list = [time.strip() for time in input_times.split(',')]

# 合計時間を計算して表示
total_time = sum_times(times_list)
print("合計時間:", total_time)
