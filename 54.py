import statistics as stat

data = [8, 17, 0, 11, 6, 21, 16, 6, 17, 11,
        7, 9, 6, 13, 12, 16, 3, 14, 13, 12]

print("平均は", stat.mean(data), "です")
print("中央値は", stat.median(data), "です")
print("最頻値は", stat.mode(data), "です")
print("分散は", stat.pvariance(data), "です")
print("標準偏差は", stat.pstdev(data), "です")
