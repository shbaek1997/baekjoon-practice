filter_minus = input().split("-")
ans = 0
first_part = list(map(int, filter_minus[0].split("+")))
ans += sum(first_part)
for i in filter_minus[1:]:
    next_part = list(map(int, i.split("+")))
    ans -= sum(next_part)
print(ans)
