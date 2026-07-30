Overview
Focuses on Data Cleaning, Exploratory Data Analysis (EDA), Data Visualization, and a Promotion Eligibility System using Python. The analyzes an employee performance dataset to discover trends, improve data quality, and generate business insights.
Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn

Dataset Information
The dataset contains employee performance records with more than 100 entries.
Columns Included
Employee ID
Name
Department
Age
Gender
Experience (Years)
Monthly Salary
Attendance (%)
Performance Score
Overtime Hours
Projects Completed
Training Hours
Remote Work Days
Job Level
Notes


1. Data Cleaning
Removed duplicate records.
Checked and handled missing values.
Converted incorrect data types to numeric format.
Standardized department names.
Removed unnecessary columns.
Detected and removed salary outliers using the IQR method.

2. Exploratory Data Analysis (EDA)
Displayed dataset information.
Generated summary statistics.
Created a correlation matrix.
Grouped employees by department.
Filtered employees with attendance below 75%.
Identified the department with the highest average performance score.

3. Performance Index
A custom Performance Index was created using the following formula:
Performance Index =
(Performance Score × 0.5)
+ (Projects Completed × 2)
+ (Attendance × 0.3)
This index was used to compare employee performance.
4. Promotion Eligibility System

Employees were classified into three categories:

Promoted
Performance Index is at least 80
Attendance is at least 90%
Projects Completed is at least 8

Requires Training
Performance Index is at least 60
Training Hours are at least 20

Needs Improvement
Employees who do not satisfy the above conditions.

Visualizations Created

Employees by Department
Monthly Salary Distribution
Performance Score Box Plot
Attendance vs Performance Scatter Plot
Average Salary by Experience
Correlation Heatmap
Average Performance by Department
Promotion Eligibility Pie Chart

Output Files
employee_performance_raw_dataset.csv
Original dataset.
employee_performance_cleaned_dataset.csv
Dataset after cleaning and preprocessing.
employee_performance_final_dataset.csv
Final dataset containing the Performance Index and Promotion Status.
Key Insights
Duplicate records were successfully removed.
Missing values were handled appropriately.
Salary outliers were removed.
Departments were compared based on average performance.
Employees with low attendance were identified.
A custom Performance Index was created for evaluation.
Promotion recommendations were generated using rule based logic.

How to Run
Open the project in Visual Studio Code or any Python IDE.
Install the required libraries:
pip install pandas numpy matplotlib seaborn
Run the Python script:
python employee_performance_eda.py
The program will:
Load the dataset.
Clean the data.
Perform exploratory data analysis.
Generate visualizations.
Calculate the Performance Index.
Determine employee promotion eligibility.
Save the cleaned and final datasets.
