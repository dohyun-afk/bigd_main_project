import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic"

prices = [27,26,27,26,25]
fig,ax = plt.subplots(figsize=(7,4))
ax.plot(prices)
for i,p in enumerate(prices):
    ax.annotate(f"{p:,}",(i,p),textcoords="offset points",xytext=(0,8),ha="center")

ax.set_title("기온 예상")
fig.savefig("my_first_chart.png")