import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# قراءة وتنظيف البيانات الأساسية

df = pd.read_csv("C:/Users/alaaa/Desktop/CSV/Domestic Tourists Number  by Destination.csv", skiprows=8)

# إنشاء عمود السنة من Unnamed: 1 مع تعبئة القيم الفارغة
df["Year"] = df["Unnamed: 1"].ffill()

# حذف الصفوف التي لا تحتوي على Indicator
df = df.dropna(subset=["Indicator"])

# تعبئة الأشهر الفارغة بنفس الشهر اللي فوقها
df["Month"] = df["Month"].ffill()

# حذف الأعمدة غير المهمة
df = df.drop(columns=["Unnamed: 0", "Unnamed: 1", "المؤشر", "الشهر", "Unnamed: 48"])

# تحويل Year إلى رقم صحيح
df["Year"] = pd.to_numeric(df["Year"], errors="coerce").ffill().astype(int)

# print(df.head())
# print(df.shape)


#  تجهيز جدول الإجمالي على مستوى المملكة
df_total = df[["Month", "Indicator", "الإجمالي", "Year"]].copy()

# فصل عدد السياح عن الإنفاق
df_total_num = df_total[df_total["Indicator"].str.contains("Number")]
df_total_spend = df_total[df_total["Indicator"].str.contains("Spending")]

# دمج الجدولين بناءً على الشهر
df_reg = df_total_num[["Month", "الإجمالي"]].merge(
    df_total_spend[["Month", "الإجمالي"]],
    on="Month",
    suffixes=("_num", "_spend")
)

# تحويل الأعمدة النصية إلى أرقام مع إجبار القيم الغريبة إلى NaN
df_reg["الإجمالي_num"] = pd.to_numeric(df_reg["الإجمالي_num"], errors="coerce")
df_reg["الإجمالي_spend"] = pd.to_numeric(df_reg["الإجمالي_spend"], errors="coerce")

# حذف أي صف فيه NaN في X أو y
df_reg = df_reg.dropna(subset=["الإجمالي_num", "الإجمالي_spend"])

print("df_reg بعد التنظيف:")
print(df_reg)
print("عدد الصفوف بعد التنظيف:", df_reg.shape[0])


#  بناء نموذج الانحدار الخطي

X = df_reg[["الإجمالي_num"]].values   # X لازم يكون 2D
y = df_reg["الإجمالي_spend"].values   # y يكون 1D

model = LinearRegression()
model.fit(X, y)
# ايجاد القيم min , max , mean , median لكلا المتغيرين

min_tourists = df_reg["الإجمالي_num"].min()
max_tourists = df_reg["الإجمالي_num"].max()
mean_tourists = df_reg["الإجمالي_num"].mean()
median_tourists = df_reg["الإجمالي_num"].median()

min_spend = df_reg["الإجمالي_spend"].min()
max_spend = df_reg["الإجمالي_spend"].max()
mean_spend = df_reg["الإجمالي_spend"].mean()
median_spend = df_reg["الإجمالي_spend"].median()

print("Tourist Numbers:")
print("Min:", min_tourists)
print("Max:", max_tourists)
print("Mean:", mean_tourists)
print("Median:", median_tourists)

print("\nTourism Spending:")
print("Min:", min_spend)
print("Max:", max_spend)
print("Mean:", mean_spend)
print("Median:", median_spend)







print("\nنتائج نموذج الانحدار:")
print("Coefficient (slope):", model.coef_[0])
print("Intercept:", model.intercept_)
print("R² Score:", model.score(X, y))



plt.figure(figsize=(10,6))
plt.plot(df_reg["Month"], df_reg["الإجمالي_num"], marker='o')
plt.title("Total Tourists per Month (2023)")
plt.xlabel("Month")
plt.ylabel("Total Tourists")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


plt.figure(figsize=(10,6))
plt.plot(df_reg["Month"], df_reg["الإجمالي_spend"], marker='o', color="gray")
plt.title("Total Tourism Spending per Month (2023)")
plt.xlabel("Month")
plt.ylabel("Total Spending (SAR)")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()



plt.figure(figsize=(10,6))
plt.scatter(X, y, color='blue')

# regression line
y_pred = model.predict(X)
plt.plot(X, y_pred, color='black')

plt.title("Regression: Tourists Number vs Tourism Spending")
plt.xlabel("Total Tourists")
plt.ylabel("Total Spending (SAR)")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()



plt.figure(figsize=(10,6))
plt.bar(df_reg["Month"], df_reg["الإجمالي_num"], color='steelblue')
plt.title("Monthly Tourist Count Comparison (2023)")
plt.xlabel("Month")
plt.ylabel("Total Tourists")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(10,6))
plt.bar(df_reg["Month"], df_reg["الإجمالي_spend"], color='gray')
plt.title("Monthly Tourism Spending Comparison (2023)")
plt.xlabel("Month")
plt.ylabel("Total Spending (SAR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


fig, ax1 = plt.subplots(figsize=(10,6))

ax1.set_xlabel("Month")
ax1.set_ylabel("Total Tourists", color='blue')
ax1.plot(df_reg["Month"], df_reg["الإجمالي_num"], color='blue', marker="o")
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
ax2.set_ylabel("Total Spending (SAR)", color='gray')
ax2.plot(df_reg["Month"], df_reg["الإجمالي_spend"], color='gray', marker="o")
ax2.tick_params(axis='y', labelcolor='gray')

plt.title("Tourists & Spending Trends (2023)")
plt.tight_layout()
plt.show()