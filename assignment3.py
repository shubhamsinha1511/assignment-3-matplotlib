# ===============================
# ASSIGNMENT 3 - COMPLETE CODE
# ===============================

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -------------------------------
# 1. Line Chart (Alphabet Inc.)
# -------------------------------
data1 = {
    "Date": ["10-03-16","10-04-16","10-05-16","10-06-16","10-07-16"],
    "Open": [774.25,776.03,779.31,779,779.66],
    "High": [776.06,778.71,782.07,780.48,779.66],
    "Low": [769.5,772.89,775.65,775.54,770.75],
    "Close": [772.56,776.43,776.47,776.86,775.08]
}

df1 = pd.DataFrame(data1)

plt.figure()
plt.plot(df1["Date"], df1["Open"], label="Open")
plt.plot(df1["Date"], df1["High"], label="High")
plt.plot(df1["Date"], df1["Low"], label="Low")
plt.plot(df1["Date"], df1["Close"], label="Close")
plt.title("Alphabet Inc Stock Prices")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()

# -------------------------------
# 2. Horizontal Bar Plot
# -------------------------------
nos = [2, 9, 20, 25, 30, 39]
marks = [12, 24, 25, 27, 29, 30]

plt.figure()
plt.barh(nos, marks)
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Students vs Marks")
plt.show()

# -------------------------------
# 3. Year-wise Sales
# -------------------------------
months = ["Jan","Feb","Mar","Apr","May","Jun"]

y2018 = [2500,2200,3000,2800,2750,3500]
y2019 = [2600,1800,2500,3000,3200,2000]
y2020 = [2450,2000,3000,3100,1950,3550]
y2021 = [3250,3200,3800,2800,2900,2300]

plt.figure()
plt.plot(months, y2018, label="2018")
plt.plot(months, y2019, label="2019")
plt.plot(months, y2020, label="2020")
plt.plot(months, y2021, label="2021")
plt.title("Year-Wise Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.show()

# -------------------------------
# 4. Customized Line Chart
# -------------------------------
plt.figure()
plt.plot(months, y2018, marker="*", markersize=10, linestyle="--", linewidth=3)
plt.title("Customized Sales Chart")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

# -------------------------------
# 5. Bar Chart (Employee Data)
# -------------------------------
dept = ["HR","Sales","Finance","Marketing","IT"]
emp = [40,30,35,32,45]

plt.figure()
plt.bar(dept, emp)
plt.title("Compu-Tech Employee Data")
plt.xlabel("Departments")
plt.ylabel("Number of Employees")
plt.show()

# -------------------------------
# 6. Scatter + Bar (Region)
# -------------------------------
data2 = {
    "Region": ["North","South","East","West","North","South","East","West"],
    "Population": [100,120,80,90,110,130,85,95],
    "Literacy": [75,80,70,72,78,82,74,76]
}

df2 = pd.DataFrame(data2)

plt.figure()
regions = df2["Region"].unique()
for r in regions:
    d = df2[df2["Region"] == r]
    plt.scatter(d["Population"], d["Literacy"], label=r)

plt.xlabel("Population")
plt.ylabel("Literacy Rate")
plt.legend()
plt.show()

plt.figure()
df2.groupby("Region")["Literacy"].mean().plot(kind="bar")
plt.title("Average Literacy Rate")
plt.show()

# -------------------------------
# 7. Boxplot (Marks)
# -------------------------------
data3 = {
    "Maths": [78,85,90,76,88],
    "Science": [82,79,88,84,91],
    "English": [74,80,85,78,83],
    "Computer": [90,92,94,89,95]
}

df3 = pd.DataFrame(data3)

plt.figure()
df3.boxplot()
plt.title("Subject-wise Performance")
plt.show()

# -------------------------------
# 8. Bar Plot (Men vs Women)
# -------------------------------
men = (22, 30, 35, 35, 26)
women = (25, 32, 30, 35, 29)

x = np.arange(len(men))
width = 0.35

plt.figure()
plt.bar(x, men, width, label="Men")
plt.bar(x + width, women, width, label="Women")
plt.xlabel("Groups")
plt.ylabel("Scores")
plt.title("Scores by Person")
plt.legend()
plt.show()

# -------------------------------
# 9. Pie Chart (Sales)
# -------------------------------
data4 = {
    "Product": ["Facewash", "Facecream", "Toothpaste", "Bathingsoap", "Shampoo"],
    "Sales": [4050, 7500, 6300, 8700, 5700]
}

df4 = pd.DataFrame(data4)

plt.figure()
plt.pie(df4["Sales"], labels=df4["Product"], autopct="%1.1f%%")
plt.title("Total Sales Percentage")
plt.show()

# -------------------------------
# 9(b). Subplots
# -------------------------------
months_num = list(range(1,13))
soap = [9000,6000,9500,8500,7500,7200,9000,10000,8000,10500,13000,14000]
facewash = [1500,1200,1350,1100,1750,1550,1100,1400,1780,1850,2100,1750]

plt.figure()
plt.subplot(2,1,1)
plt.plot(months_num, soap)
plt.title("Bathing Soap Sales")

plt.subplot(2,1,2)
plt.plot(months_num, facewash)
plt.title("Facewash Sales")

plt.show()

# -------------------------------
# 10. Histogram
# -------------------------------
profit = [200000,220000,210000,250000,270000,300000,320000,180000]

plt.figure()
plt.hist(profit)
plt.title("Profit Data")
plt.xlabel("Profit Range")
plt.ylabel("Frequency")
plt.show()
