#  Statistical Analysis of Temperature Patterns in Lahore

### Predicting Summer Heat Risk Using Statistics & Probability

---

##  The Scenario

Every summer, Lahore faces extreme heat — but how hot is it really, and what is the **probability** of a dangerous heat day on any given date in June?

This project applies core concepts from **Introductory Statistics (Neil A. Weiss)** to answer that real-life question using 30 days of June temperature data.

---

##  The Problem

> *"If I step outside tomorrow in June, what is the probability it will be dangerously hot in Lahore?"*

This is a genuine everyday-life problem — affecting decisions about going outdoors, water consumption, electricity load-shedding schedules, and public health advisories.

---

##  Statistical Concepts Applied

| Concept | Chapter | Used For |
|---|---|---|
| Frequency Distribution | Ch 2 | Organizing 30 days of data into classes |
| Mean, Median, Mode | Ch 3 | Finding the typical June temperature |
| Variance & Standard Deviation | Ch 3 | Measuring temperature consistency |
| Z-Scores | Ch 3 | Identifying how extreme specific days were |
| Quartiles, IQR & Outliers | Ch 3 | Detecting unusual temperature days |
| Classical Probability | Ch 5 | Calculating real chance of heat events |
| Complement & Addition Rules | Ch 5 | Probability of NOT exceeding a threshold |
| Normal Distribution | Ch 8 | Modeling temperature as a continuous distribution |
| Empirical Rule (68-95-99.7) | Ch 8 | Understanding spread of temperatures |
| Confidence Interval (Z-Interval) | Ch 8 | Estimating the true mean June temperature |

---

##  Key Results

| Metric | Value |
|---|---|
| Sample Size (n) | 30 days |
| Mean Temperature | 41.43°C |
| Median | 41.5°C |
| Mode | 43°C |
| Standard Deviation | 2.36°C |
| Coefficient of Variation | 5.69% |
| P(Temperature > 40°C) | 72.83% |
| P(Temperature > 45°C — Danger Level) | 6.53% |
| 95% Confidence Interval for Mean | (40.59°C, 42.28°C) |
| Outliers Detected | None |

---

## Visualizations

This project generates **6 charts**:
1. Daily Temperature Trend (Line Graph)
2. Frequency Histogram
3. Normal Distribution Curve with Shaded Probabilities
4. Box Plot (Five-Number Summary)
5. Pie Chart — Temperature Category Distribution
6. Probability Bar Chart — Heat Event Likelihoods

---

##  How to Run

```bash
pip install numpy matplotlib scipy
python temperature_stats_alisha_sultan.py
```

The script prints a full statistical breakdown to the terminal and saves all 6 graphs as PNG images in the same folder.

---

##  Conclusion

- Lahore's June temperatures are consistent and predictable (low CV = 5.69%)
- There is a **72.83% probability** any given June day exceeds 40°C
- Only a **6.53% probability** of reaching the dangerous 45°C+ threshold
- The 95% Confidence Interval confirms the true average June temperature lies between **40.59°C and 42.28°C**
- This proves statistics can guide real public health, water, and electricity planning decisions — not just academic theory

---

##  Tools Used

- **Python** — NumPy, SciPy, Matplotlib
- **Statistical Concepts** — Weiss, *Introductory Statistics* (Chapters 2, 3, 5, 8)

---

##  Acknowledgement

**Thank You Sir: Fakhar Mustafa**
Course: Introduction to Statistics & Probability

---

##  Author

**Alisha Sultan**
Registration No: FA25-BMD-028
BS Mathematics with Data Science — 2nd Semester
COMSATS University Islamabad, Sahiwal Campus

---

#Statistics #Python #Probability #DataScience #NormalDistribution #ConfidenceInterval #COMSATS #Mathematics
