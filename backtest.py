import pyupbit
import numpy as np

# open(시가), high(고가), low(저가), close(종가)
# volume(거래량), range(변동폭*k), target(매수가)
# ror(수익률), hpr(누적 수익률), dd(낙폭)

df = pyupbit.get_ohlcv("KRW-BTC", count = 7)
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)


df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)

df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD(%): ", df['dd'].max())
df.to_excel("dd.xlsx")