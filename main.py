import pandas as pd
import matplotlib.pyplot as plt

data2018 = pd.read_csv(r"C:\Users\keema\Downloads\2018 nba - 시트1.csv")
data2020 = pd.read_csv(r"C:\Users\keema\Downloads\2020 nba - Sheet1 (1).csv")

# 2018 home vs away wr
# df = pd.DataFrame(data2018, columns=["TEAM", "home winrate", "away winrate"])
# df.plot(x="TEAM", y=["home winrate", "away winrate"], kind="bar", figsize=(9, 8))
#
# plt.waitforbuttonpress()
# plt.show()

# 2018 home vs away fans attendance
# df = pd.DataFrame(data2018, columns=["TEAM", "home fans", "away fans"])
# df.plot(x="TEAM", y=["home fans", "away fans"], kind="bar", figsize=(9, 8))
#
# plt.waitforbuttonpress()
# plt.show()

# 2020 home vs away wr
# df = pd.DataFrame(data2020, columns=["TEAM", "home", "away"])
# df.plot(x="TEAM", y=["home", "away"], kind="bar", figsize=(6.4, 4.8))
#
# plt.waitforbuttonpress()
# plt.show()