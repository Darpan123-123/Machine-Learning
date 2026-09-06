# -*- coding: utf-8 -*-
"""
Week 1 Lab Assignment: Python, NumPy, Pandas, & Matplotlib
Filename: lastname_week1_lab.py
Course: Machine Learning Foundations
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Check if student_data.csv exists, otherwise create it for demonstration
if not os.path.exists("student_data.csv"):
    # Generate some mock data for Q19 and Q22
    np.random.seed(42)
    names = ["Aarav", "Ananya", "Vihaan", "Diya", "Sai", "Kabir", "Meera", "Rohan"]
    sections = ["A", "B", "A", "C", "B", "A", "C", "B"]
    marks = [45, 88, 92, 35, 76, np.nan, 62, 55]  # contains one NaN for cleaning demo
    df_students = pd.DataFrame({
        "student_id": [101, 102, 103, 104, 105, 106, 107, 108],
        "name": names,
        "section": sections,
        "marks": marks
    })
    df_students.to_csv("student_data.csv", index=False)

    df_attendance = pd.DataFrame({
        "student_id": [101, 102, 103, 104, 105, 106, 107, 108],
        "attendance": [80.0, 95.0, 68.0, 72.0, 90.0, 85.0, 60.0, 88.0]
    })
    df_attendance.to_csv("attendance_data.csv", index=False)




# ----------------------------------------------------------------------
# Q1: Write a program that swaps the values of two variables without 
#     using a third variable.
# ----------------------------------------------------------------------
print("\n[Q1] Swapping two variables without a third variable:")
a = 15
b = 42
print(f"Before swap: a = {a}, b = {b}")
# Using Python's tuple unpacking to swap values in-place
a, b = b, a
print(f"After swap: a = {a}, b = {b}")


# ----------------------------------------------------------------------
# Q2: Write a function is_prime(n) that returns True if n is a prime 
#     number, otherwise False.
# ----------------------------------------------------------------------
print("\n[Q2] Checking prime numbers:")
def is_prime(n):
    """
    Returns True if n is a prime number, otherwise False.
    Optimized to run in O(sqrt(n)) time complexity.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Check divisors up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Testing is_prime function with a few numbers
test_nums = [2, 11, 15, 29, 33, 100]
prime_results = {num: is_prime(num) for num in test_nums}
print("Prime check results:", prime_results)


# ----------------------------------------------------------------------
# Q3: Write a program to print the Fibonacci sequence up to n terms 
#     using a loop.
# ----------------------------------------------------------------------
print("\n[Q3] Fibonacci sequence up to n terms:")
def fibonacci(n):
    """Generates the Fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    seq = [0, 1]
    # Loop to add previous two numbers to generate the next term
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

n_terms = 10
print(f"Fibonacci sequence ({n_terms} terms): {fibonacci(n_terms)}")


# ----------------------------------------------------------------------
# Q4: Write a function that takes a list of numbers and returns a new 
#     list with duplicates removed, preserving order.
# ----------------------------------------------------------------------
print("\n[Q4] Removing duplicates while preserving order:")
def remove_duplicates(lst):
    """
    Removes duplicate elements from a list while keeping the original 
    element order intact. Uses a set to track seen elements in O(1) time.
    """
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

duplicate_list = [5, 2, 9, 2, 5, 1, 9, 7, 10, 5]
print(f"Original list: {duplicate_list}")
print(f"Deduplicated list: {remove_duplicates(duplicate_list)}")


# ----------------------------------------------------------------------
# Q5: Write a function multiply(*args) that returns the product of 
#     any number of arguments using *args.
# ----------------------------------------------------------------------
print("\n[Q5] Variable arguments multiplication function:")
def multiply(*args):
    """
    Multiplies any number of arguments passed dynamically using *args.
    Returns 0 if no arguments are provided.
    """
    if not args:
        return 0
    product = 1
    for num in args:
        product *= num
    return product

print(f"multiply(2, 3, 4)       -> {multiply(2, 3, 4)}")
print(f"multiply(5, 10, 0.5, 4) -> {multiply(5, 10, 0.5, 4)}")


# ----------------------------------------------------------------------
# Q6: Write a dictionary comprehension mapping each character in a 
#     string to its frequency.
# ----------------------------------------------------------------------
print("\n[Q6] Character frequency mapping via dictionary comprehension:")
sample_string = "machine learning"
# Comprehension iterates over the string and counts character occurrences
char_freq = {char: sample_string.count(char) for char in sample_string if char != ' '}
print(f"String: '{sample_string}'")
print(f"Character frequencies (excluding spaces): {char_freq}")


# ----------------------------------------------------------------------
# Q7: Given a list of dictionaries representing employees (name, 
#     department, salary), find the employee with the highest salary.
# ----------------------------------------------------------------------
print("\n[Q7] Employee with the highest salary:")
employees = [
    {"name": "Amit", "department": "Data Science", "salary": 95000},
    {"name": "Pooja", "department": "Engineering", "salary": 115000},
    {"name": "Vikram", "department": "Marketing", "salary": 80000},
    {"name": "Neha", "department": "Product", "salary": 125000}
]

# Finding the dictionary with the maximum salary value
highest_paid = max(employees, key=lambda emp: emp["salary"])
print(f"Highest Paid Employee: {highest_paid['name']} ({highest_paid['department']}) "
      f"- Salary: Rs. {highest_paid['salary']}")


# ----------------------------------------------------------------------
# Q8: Write a lambda function combined with filter() to extract 
#     all odd numbers from a list.
# ----------------------------------------------------------------------
print("\n[Q8] Filtering odd numbers using lambda and filter():")
num_list = [14, 21, 35, 42, 57, 68, 79, 90]
# Lambda returns True if the number is odd (num % 2 != 0)
odd_numbers = list(filter(lambda x: x % 2 != 0, num_list))
print(f"Original list: {num_list}")
print(f"Filtered odd numbers: {odd_numbers}")


print("\n" + "="*60)
print("                   SECTION B — NUMPY (Q9–Q17)                  ")
print("="*60)

# ----------------------------------------------------------------------
# Q9: Create a 1D NumPy array of integers from 1 to 30 and reshape 
#     it into a 5x6 matrix.
# ----------------------------------------------------------------------
print("\n[Q9] Reshaping 1D NumPy array into 5x6 matrix:")
array_1d = np.arange(1, 31)
matrix_5x6 = array_1d.reshape(5, 6)
print("Original 1D Array:\n", array_1d)
print("Reshaped 5x6 Matrix:\n", matrix_5x6)


# ----------------------------------------------------------------------
# Q10: Create a 6x6 identity matrix and replace its diagonal with 
#      the values [1,2,3,4,5,6].
# ----------------------------------------------------------------------
print("\n[Q10] Replacing identity matrix diagonal with custom values:")
identity_matrix = np.eye(6)
print("Original 6x6 Identity Matrix:\n", identity_matrix)

# np.diag_indices_from(matrix) returns the indices to access the diagonal elements
diagonal_values = [1, 2, 3, 4, 5, 6]
identity_matrix[np.diag_indices_from(identity_matrix)] = diagonal_values
print("Modified Matrix with Custom Diagonal [1,2,3,4,5,6]:\n", identity_matrix)


# ----------------------------------------------------------------------
# Q11: Given a NumPy array of 25 random integers between 1 and 100, 
#      find the sum, mean, and standard deviation.
# ----------------------------------------------------------------------
print("\n[Q11] Statistical analysis on 25 random integers:")
np.random.seed(10)  # Seed for reproducible results
random_ints = np.random.randint(1, 101, size=25)
print("Generated Array:\n", random_ints)
print(f"Sum: {np.sum(random_ints)}")
print(f"Mean: {np.mean(random_ints):.2f}")
print(f"Standard Deviation: {np.std(random_ints):.2f}")


# ----------------------------------------------------------------------
# Q12: Given a 2D array of shape (4,4), extract the diagonal elements 
#      using np.diag() and compute their sum.
# ----------------------------------------------------------------------
print("\n[Q12] Diagonal extraction and summation:")
matrix_4x4 = np.array([
    [10, 15, 20, 25],
    [30, 40, 50, 60],
    [70, 80, 90, 100],
    [110, 120, 130, 140]
])
print("Original 4x4 Matrix:\n", matrix_4x4)
diag_elements = np.diag(matrix_4x4)
diag_sum = np.sum(diag_elements)
print(f"Extracted Diagonal Elements: {diag_elements}")
print(f"Sum of Diagonal Elements: {diag_sum}")


# ----------------------------------------------------------------------
# Q13: Create two arrays of shape (3,3) and demonstrate the difference 
#      between element-wise multiplication (*) and matrix multiplication (@).
# ----------------------------------------------------------------------
print("\n[Q13] Element-wise (*) vs. Matrix Multiplication (@):")
arr_A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
arr_B = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

element_wise = arr_A * arr_B
matrix_mul = arr_A @ arr_B

print("Array A:\n", arr_A)
print("Array B:\n", arr_B)
print("Element-wise Multiplication (arr_A * arr_B):\n", element_wise)
print("Matrix Multiplication (arr_A @ arr_B):\n", matrix_mul)


# ----------------------------------------------------------------------
# Q14: Given an array of daily temperatures for a month, use boolean 
#      masking to find and count days above 35°C.
# ----------------------------------------------------------------------
print("\n[Q14] Temperature analysis using boolean masking (>35°C):")
np.random.seed(15)
# Simulating a month of 30 days with temperatures between 25°C and 45°C
monthly_temps = np.random.randint(25, 46, size=30)
print("Monthly Temperatures:\n", monthly_temps)

# Mask checks which temperatures are strictly greater than 35
hot_days_mask = monthly_temps > 35
hot_days_temps = monthly_temps[hot_days_mask]
count_hot_days = np.sum(hot_days_mask)

print(f"Temperatures on Hot Days (>35°C): {hot_days_temps}")
print(f"Total Hot Days: {count_hot_days} out of 30 days")


# ----------------------------------------------------------------------
# Q15: Write NumPy code to normalize an array to the range 0–1 using 
#      (x - min) / (max - min).
# ----------------------------------------------------------------------
print("\n[Q15] Min-Max scaling normalization:")
raw_scores = np.array([120, 340, 250, 480, 190, 500, 310])
print("Original Array:", raw_scores)

# Normalization formula application
min_val = np.min(raw_scores)
max_val = np.max(raw_scores)
normalized_scores = (raw_scores - min_val) / (max_val - min_val)

print(f"Normalized Array (range 0 to 1):\n", np.round(normalized_scores, 4))


# ----------------------------------------------------------------------
# Q16: Given a 2D array of shape (5,3) (5 students, 3 subjects), 
#      compute total and average marks per student using axis-based aggregation.
# ----------------------------------------------------------------------
print("\n[Q16] Axis-based aggregation for student statistics:")
# 5 students (rows) x 3 subjects (columns)
student_marks = np.array([
    [75, 80, 85],  # Student 1
    [90, 92, 88],  # Student 2
    [60, 65, 70],  # Student 3
    [85, 75, 95],  # Student 4
    [40, 50, 45]   # Student 5
])
print("Marks Matrix (5 Students x 3 Subjects):\n", student_marks)

# axis=1 aggregates across columns (along each row/student)
total_marks = np.sum(student_marks, axis=1)
avg_marks = np.mean(student_marks, axis=1)

for idx in range(5):
    print(f"Student {idx+1}: Total = {total_marks[idx]}, Average = {avg_marks[idx]:.2f}")


# ----------------------------------------------------------------------
# Q17: Use np.where() to replace all even numbers in an array with -1, 
#      keeping odd numbers unchanged.
# ----------------------------------------------------------------------
print("\n[Q17] Replacing even values with -1 using np.where():")
test_array = np.array([12, 15, 22, 29, 34, 41, 56, 63])
print("Original Array:", test_array)

# If condition test_array % 2 == 0 is True, replace with -1, else keep element
modified_array = np.where(test_array % 2 == 0, -1, test_array)
print("Modified Array (even numbers replaced with -1):", modified_array)


print("\n" + "="*60)
print("                   SECTION C — PANDAS (Q18–Q22)                ")
print("="*60)

# ----------------------------------------------------------------------
# Q18: Create a DataFrame of 8 students with columns name, section, 
#      and marks; print df.describe().
# ----------------------------------------------------------------------
print("\n[Q18] Creating student DataFrame and descriptive statistics:")
names_list = ["Aarav", "Ananya", "Vihaan", "Diya", "Sai", "Kabir", "Meera", "Rohan"]
sections_list = ["A", "B", "A", "C", "B", "A", "C", "B"]
marks_list = [45, 88, 92, 35, 76, 50, 62, 55]

df = pd.DataFrame({
    "student_id": [101, 102, 103, 104, 105, 106, 107, 108],
    "name": names_list,
    "section": sections_list,
    "marks": marks_list
})
print("Students DataFrame:\n", df)
print("\nDescriptive Statistics (df.describe()):\n", df.describe())


# ----------------------------------------------------------------------
# Q19: Load a provided CSV, report how many missing values exist 
#      per column, and fill numeric missing values with the column mean.
# ----------------------------------------------------------------------
print("\n[Q19] Handling missing values in loaded CSV:")
# Loading the generated CSV file
loaded_df = pd.read_csv("student_data.csv")
print("Loaded DataFrame with missing values:\n", loaded_df)

# Check missing values per column
missing_counts = loaded_df.isna().sum()
print("\nMissing values count per column:\n", missing_counts)

# Filling numeric missing values ('marks') with the mean of that column
mean_marks = loaded_df["marks"].mean()
loaded_df["marks"] = loaded_df["marks"].fillna(mean_marks)
print(f"\nFilled missing 'marks' with column mean: {mean_marks:.2f}")
print("Cleaned DataFrame:\n", loaded_df)


# ----------------------------------------------------------------------
# Q20: Using .loc and boolean filtering, select all rows where marks 
#      are below 50 and print only the name and marks columns.
# ----------------------------------------------------------------------
print("\n[Q20] Boolean filtering with .loc (<50 marks):")
# Filtering using labels and conditional mask
below_50_df = loaded_df.loc[loaded_df["marks"] < 50, ["name", "marks"]]
print("Students with marks below 50:\n", below_50_df)


# ----------------------------------------------------------------------
# Q21: Group the students DataFrame by 'section' and compute the 
#      mean and max marks per section.
# ----------------------------------------------------------------------
print("\n[Q21] Groupby section and aggregating statistics:")
# Performing aggregation (mean & max) grouped by the 'section' column
section_stats = loaded_df.groupby("section")["marks"].agg(["mean", "max"])
print("Section Stats:\n", section_stats)


# ----------------------------------------------------------------------
# Q22: Given two DataFrames — students and their attendance — merge 
#      them on student ID and report students with attendance below 75%.
# ----------------------------------------------------------------------
print("\n[Q22] Merging DataFrames and filtering low attendance (<75%):")
# Loading or creating attendance DataFrame
attendance_df = pd.read_csv("attendance_data.csv") if os.path.exists("attendance_data.csv") else pd.DataFrame({
    "student_id": [101, 102, 103, 104, 105, 106, 107, 108],
    "attendance": [80.0, 95.0, 68.0, 72.0, 90.0, 85.0, 60.0, 88.0]
})

print("Attendance DataFrame:\n", attendance_df)

# Merging students dataframe with attendance dataframe on 'student_id'
merged_df = pd.merge(loaded_df, attendance_df, on="student_id")
print("\nMerged DataFrame:\n", merged_df)

# Filter students with attendance below 75%
low_attendance = merged_df[merged_df["attendance"] < 75.0]
print("\nStudents with attendance below 75%:\n", low_attendance[["name", "attendance"]])


print("\n" + "="*60)
print("                 SECTION D — MATPLOTLIB (Q23–Q25)              ")
print("="*60)

# Setting non-interactive backend for headless environments
plt.switch_backend('Agg')

# ----------------------------------------------------------------------
# Q23: Plot a bar chart of average marks per section (from Q21's 
#      groupby result) with labeled axes and a title.
# ----------------------------------------------------------------------
print("\n[Q23] Generating Section-wise Average Marks Bar Chart...")
fig1, ax1 = plt.subplots(figsize=(6, 4))
sections = section_stats.index
mean_marks_per_sec = section_stats["mean"]

bars = ax1.bar(sections, mean_marks_per_sec, color="steelblue", edgecolor="black", width=0.5)
ax1.set_xlabel("Section", fontsize=11, fontweight='bold', labelpad=8)
ax1.set_ylabel("Average Marks", fontsize=11, fontweight='bold', labelpad=8)
ax1.set_title("Section-wise Average Marks", fontsize=12, fontweight='bold', pad=15)
ax1.set_ylim(0, 100)

# Add numeric value labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 2, f"{yval:.1f}", ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig("q23_bar_chart.png", dpi=150)
plt.close()
print("Success: Bar chart saved as 'q23_bar_chart.png'")


# ----------------------------------------------------------------------
# Q24: Plot a histogram of the marks column from your DataFrame and 
#      describe the shape of the distribution in one sentence.
# ----------------------------------------------------------------------
print("\n[Q24] Generating Student Marks Histogram...")
fig2, ax2 = plt.subplots(figsize=(6, 4))
ax2.hist(loaded_df["marks"], bins=5, color="teal", edgecolor="black", alpha=0.8)
ax2.set_xlabel("Marks Range", fontsize=11, fontweight='bold', labelpad=8)
ax2.set_ylabel("Number of Students (Frequency)", fontsize=11, fontweight='bold', labelpad=8)
ax2.set_title("Distribution of Student Marks", fontsize=12, fontweight='bold', pad=15)
ax2.set_xlim(30, 100)
ax2.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig("q24_histogram.png", dpi=150)
plt.close()
print("Success: Histogram saved as 'q24_histogram.png'")
print("Analysis sentence: The distribution of student marks is bimodal, with peaks at "
      "both the lower end (35-50 marks) and the higher end (75-95 marks), showing distinct "
      "performing cohorts in the class.")


# ----------------------------------------------------------------------
# Q25: Create a 1x2 subplot showing a line plot of any numeric trend 
#      on the left and a scatter plot of two numeric columns on the right.
# ----------------------------------------------------------------------
print("\n[Q25] Generating 1x2 Subplot (Line plot & Scatter plot)...")
fig3, (ax_line, ax_scatter) = plt.subplots(1, 2, figsize=(12, 5))

# Left Subplot: Line plot representing attendance trend across index
ax_line.plot(merged_df["name"], merged_df["attendance"], marker='o', color="crimson", linewidth=2, label="Attendance %")
ax_line.set_xlabel("Student Name", fontsize=10, fontweight='bold')
ax_line.set_ylabel("Attendance (%)", fontsize=10, fontweight='bold')
ax_line.set_title("Student Attendance Trend", fontsize=11, fontweight='bold', pad=10)
ax_line.set_ylim(50, 100)
ax_line.tick_params(axis='x', rotation=45)
ax_line.grid(True, linestyle=':', alpha=0.6)

# Right Subplot: Scatter plot representing Study Hours (simulated) vs Marks
study_hours = [3, 8, 9, 2, 7, 5, 6, 4]  # simulated feature
ax_scatter.scatter(study_hours, merged_df["marks"], color="darkblue", s=80, edgecolor="orange", alpha=0.9)
ax_scatter.set_xlabel("Weekly Study Hours (Simulated)", fontsize=10, fontweight='bold')
ax_scatter.set_ylabel("Exam Marks", fontsize=10, fontweight='bold')
ax_scatter.set_title("Study Hours vs Exam Marks", fontsize=11, fontweight='bold', pad=10)
ax_scatter.set_xlim(0, 11)
ax_scatter.set_ylim(20, 100)
ax_scatter.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.savefig("q25_subplots.png", dpi=150)
plt.close()
