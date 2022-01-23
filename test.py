import pyupbit

access = "TfqSyt63ZOqXKNW1bHtFANOB1Z8cI6kd28gDBHaI"          # 본인 값으로 변경
secret = "TOZICn31KPvuAfnqqg2QUBU5yjGuwXJxLbxLxK6B"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BCT"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
