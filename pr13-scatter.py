import matplotlib.pyplot as plt
advertising_spending = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
sales_revenue = [45, 52, 63, 58, 70, 74, 85, 90, 95, 98]
plt.scatter(advertising_spending, sales_revenue, c='blue', label='Data Points', alpha=0.7)
plt.title('Advertising Spending vs. Sales Revenue')
plt.xlabel('Advertising Spending (in $1000s)')
plt.ylabel('Sales Revenue (in $1000s)')
plt.grid(True)
plt.legend()
plt.show()
