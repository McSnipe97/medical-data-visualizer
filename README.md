In this project, we visualize and make calculations from medical examination data using matplotlib, seaborn, and pandas. The dataset values were collected during medical examinations.

#### Data description

The rows in the dataset represent patiets and the columns represent information like body measurements, results from various blood tests, and lifestyle choices. We will use the dataset to exploring the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.

File name: medical_examination.csv

| Feature | Variable Type | Variable      | Value Type |
|:-------:|:------------:|:-------------:|:----------:|
| Age | Objective Feature | age | int (days) |
| Height | Objective Feature | height | int (cm) |
| Weight | Objective Feature | weight | float (kg) |
| Gender | Objective Feature | gender | categorical code |
| Systolic blood pressure | Examination Feature | ap_hi | int |
| Diastolic blood pressure | Examination Feature | ap_lo | int |
| Cholesterol | Examination Feature | cholesterol | 1: normal, 2: above normal, 3: well above normal |
| Glucose | Examination Feature | gluc | 1: normal, 2: above normal, 3: well above normal |
| Smoking | Subjective Feature | smoke | binary |
| Alcohol intake | Subjective Feature | alco | binary |
| Physical activity | Subjective Feature | active | binary |
| Presence or absence of cardiovascular disease | Target Variable | cardio | binary |
---
### To-do
Nothing! Everything is done yay!

---
### Doing
- [ ] Adding more visualization features.

---
### Done
Use the data to answer and complete the following tasks in `medical_data_visualizer.py`:

- [X] Create a chart where we show the counts of good and bad outcomes for cholesterol, gluc, alco variable, active, and smoke for patients with cardio=1 and cardio=0 in different panels.

- [X] Add an 'overweight' column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.
- [X] Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
- [X] Convert the data into long format and create a chart that shows the value counts of the categorical features using seaborn's `catplot()`. The dataset should be split by 'Cardio' so there is one chart for each 'cardio' value. The chart should look like "examples/Figure_1.png".
- [X] Clean the data. Filter out the following patient segments that represent incorrect data:
  - [X] diastolic pressure is higher then systolic (Keep the correct data with `df['ap_lo'] <= df['ap_hi'])`)
  - [X] height is less than the 2.5th percentile (Keep the correct data with `(df['height'] >= df['height'].quantile(0.025))`)
  - [X] height is more than the 97.5th percentile
  - [x] weight is less then the 2.5th percentile
  - [X] weight is more than the 97.5th percentile
- [X] Create a correlation matrix using the dataset. Plot the correlation matrix using seaborn's `heatmap()`. Mask the upper triangle. The chart should look like "examples/Figure_2.png".

Unit tests are written under `test_module.py`.

---

### Development

For development, you can use `main.py` to test functions. Just execute `main.py` script from terminal and it should run.

### Testing 

Tests from `test_module.py` to `main.py` for convenience. The tests will run automatically whenever `main.py` is run.

