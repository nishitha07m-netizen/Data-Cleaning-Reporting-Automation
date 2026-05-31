import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("raw_data.csv")

print("Original Data:")
print(df)

# Remove Duplicates
df = df.drop_duplicates()

# Handle Missing Values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Department'] = df['Department'].fillna("Unknown")
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

# Save Cleaned Data
df.to_csv("cleaned_data.csv", index=False)

# Generate Summary Report
report = {
    "Total Records": len(df),
    "Average Age": round(df['Age'].mean(), 2),
    "Average Salary": round(df['Salary'].mean(), 2),
    "Departments": df['Department'].nunique()
}

report_df = pd.DataFrame(report.items(),
                         columns=['Metric', 'Value'])

report_df.to_excel(
    "automation_report.xlsx",
    index=False
)

print("\nReport Generated Successfully!")

# Visualization
salary_by_dept = (
    df.groupby('Department')['Salary']
    .mean()
)

plt.figure(figsize=(8,5))
salary_by_dept.plot(kind='bar')

plt.title("Average Salary by Department")
plt.ylabel("Salary")
plt.xlabel("Department")

plt.tight_layout()
plt.savefig("salary_summary.png")

plt.show()