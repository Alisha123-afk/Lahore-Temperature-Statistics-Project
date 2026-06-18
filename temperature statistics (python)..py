# ============================================================
#   STATISTICAL ANALYSIS OF TEMPERATURE PATTERNS IN LAHORE
#   Predicting Summer Heat Using Statistics & Probability
# ------------------------------------------------------------
#   Student  : Alisha Sultan
#  Program  : BS Mathematics with Data Science
#   Subject  : Introduction to Statistics & Probability
# ============================================================

import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from scipy import stats

# ============================================================
#   STEP 1 — SCENARIO
# ============================================================
print("=" * 60)
print("   STATISTICAL ANALYSIS OF LAHORE SUMMER TEMPERATURES")
print("   Using Statistics & Probability — June 2024")
print("=" * 60)
print()
print("SCENARIO:")
print("  Lahore faces extreme summer heat every June.")
print("  QUESTION: What is the probability of a dangerous")
print("  heat day? Can we predict tomorrow's temperature risk?")
print("  This project uses Statistics & Probability to answer.")
print()

# ============================================================
#   STEP 2 — DATA (30 Days of June 2024, Lahore)
# ============================================================
temperatures = [
    38, 40, 39, 42, 41, 43, 39, 37, 38, 40,
    41, 44, 43, 42, 45, 44, 43, 41, 40, 42,
    43, 46, 45, 44, 43, 42, 41, 40, 39, 38
]
n = len(temperatures)

print("=" * 60)
print("   DATA — DAILY MAX TEMPERATURES (°C), JUNE 2024")
print("=" * 60)
for i in range(0, n, 6):
    row = temperatures[i:i+6]
    days = [f"Day {i+j+1}: {row[j]}°C" for j in range(len(row))]
    print("  " + "  |  ".join(days))
print()

# ============================================================
#   CHAPTER 2 — FREQUENCY DISTRIBUTION
# ============================================================
print("=" * 60)
print("   CHAPTER 2 — FREQUENCY DISTRIBUTION")
print("=" * 60)

classes     = [(37,38), (39,40), (41,42), (43,44), (45,46)]
class_names = ["37–38°C", "39–40°C", "41–42°C", "43–44°C", "45–46°C"]
freqs       = [sum(1 for t in temperatures if lo <= t <= hi) for lo,hi in classes]
midpoints   = [(lo+hi)/2 for lo,hi in classes]
rel_freqs   = [f/n for f in freqs]
cum_freqs   = []
cf = 0
for f in freqs:
    cf += f
    cum_freqs.append(cf)

print(f"  Class Width = (Max - Min) / Classes = (46-37)/5 = 2°C")
print()
print(f"  {'Class':<10} {'Midpoint':<10} {'Freq':<8} {'Rel.Freq':<12} {'Cum.Freq'}")
print("  " + "-" * 52)
for i in range(len(classes)):
    print(f"  {class_names[i]:<10} {midpoints[i]:<10} {freqs[i]:<8} {rel_freqs[i]:.4f}{'':>6} {cum_freqs[i]}")
print("  " + "-" * 52)
print(f"  {'TOTAL':<10} {'':10} {n:<8} {sum(rel_freqs):.4f}")
print()

# ============================================================
#   CHAPTER 3 — MEASURES OF CENTRAL TENDENCY
# ============================================================
print("=" * 60)
print("   CHAPTER 3 — MEASURES OF CENTRAL TENDENCY")
print("=" * 60)

# Mean
mean = sum(temperatures) / n
print(f"  Formula : x̄ = Σx / n")
print(f"  Mean    : {sum(temperatures)} / {n} = {mean:.4f}°C")
print()

# Median
sorted_temps = sorted(temperatures)
median = (sorted_temps[14] + sorted_temps[15]) / 2
print(f"  Formula : Median = (15th + 16th value) / 2  [n=30, even]")
print(f"  Median  : ({sorted_temps[14]} + {sorted_temps[15]}) / 2 = {median}°C")
print()

# Mode
from collections import Counter
mode = Counter(temperatures).most_common(1)[0][0]
mode_count = Counter(temperatures).most_common(1)[0][1]
print(f"  Mode    : {mode}°C  (appears {mode_count} times — most frequent)")
print()

print(f"  ✔ Mean ≈ Median ≈ Mode → Distribution is SYMMETRIC")
print(f"    → Normal Distribution model is valid!")
print()

# ============================================================
#   CHAPTER 3 — MEASURES OF VARIATION
# ============================================================
print("=" * 60)
print("   CHAPTER 3 — MEASURES OF VARIATION")
print("=" * 60)

# Range
rng = max(temperatures) - min(temperatures)
print(f"  Range    : Max - Min = {max(temperatures)} - {min(temperatures)} = {rng}°C")
print()

# Variance (sample)
variance = sum((x - mean)**2 for x in temperatures) / (n - 1)
print(f"  Formula  : s² = Σ(x - x̄)² / (n-1)")
print(f"  Variance : s² = {variance:.4f} °C²")
print(f"  Note     : Divided by (n-1)=29 because this is a SAMPLE")
print()

# Standard Deviation
std_dev = math.sqrt(variance)
print(f"  Formula  : s = √s²")
print(f"  Std Dev  : s = √{variance:.4f} = {std_dev:.4f}°C")
print()

# CV
cv = (std_dev / mean) * 100
print(f"  Formula  : CV = (s / x̄) × 100%")
print(f"  CV       : ({std_dev:.4f} / {mean:.4f}) × 100 = {cv:.2f}%")
print(f"  → LOW CV means temperatures are CONSISTENT throughout June")
print()

# ============================================================
#   CHAPTER 3 — Z-SCORES, QUARTILES, OUTLIERS
# ============================================================
print("=" * 60)
print("   CHAPTER 3 — Z-SCORES, QUARTILES & OUTLIER DETECTION")
print("=" * 60)

# Z-scores
z_45 = (45 - mean) / std_dev
z_37 = (37 - mean) / std_dev
print(f"  Formula  : z = (x - x̄) / s")
print(f"  z(45°C)  : (45 - {mean:.4f}) / {std_dev:.4f} = {z_45:.4f}")
print(f"             → 45°C is {z_45:.2f} standard deviations ABOVE mean")
print()
print(f"  z(37°C)  : (37 - {mean:.4f}) / {std_dev:.4f} = {z_37:.4f}")
print(f"             → 37°C is {abs(z_37):.2f} standard deviations BELOW mean")
print()

# Quartiles
q1 = float(np.percentile(temperatures, 25))
q3 = float(np.percentile(temperatures, 75))
iqr = q3 - q1
print(f"  Q1 (25th percentile) : {q1}°C")
print(f"  Q2 / Median          : {median}°C")
print(f"  Q3 (75th percentile) : {q3}°C")
print(f"  IQR = Q3 - Q1        : {q3} - {q1} = {iqr}°C")
print()

# Outlier fences
lower_fence = q1 - 1.5 * iqr
upper_fence = q3 + 1.5 * iqr
outliers    = [t for t in temperatures if t < lower_fence or t > upper_fence]
print(f"  Lower Fence : Q1 - 1.5×IQR = {q1} - {1.5*iqr} = {lower_fence}°C")
print(f"  Upper Fence : Q3 + 1.5×IQR = {q3} + {1.5*iqr} = {upper_fence}°C")
print(f"  Outliers    : {outliers if outliers else 'NONE — all values within expected range'}")
print()

# ============================================================
#   CHAPTER 5 — PROBABILITY ANALYSIS
# ============================================================
print("=" * 60)
print("   CHAPTER 5 — PROBABILITY ANALYSIS")
print("=" * 60)
print(f"  Formula : P(E) = favorable outcomes / total outcomes")
print()

p_above_40  = sum(1 for t in temperatures if t > 40) / n
p_above_45  = sum(1 for t in temperatures if t >= 45) / n
p_below_40  = 1 - p_above_40
p_40_to_43  = sum(1 for t in temperatures if 40 <= t <= 43) / n

print(f"  P(T > 40°C)         : {sum(1 for t in temperatures if t>40)}/{n} = {p_above_40:.4f} = {p_above_40*100:.2f}%")
print(f"  P(T ≤ 40°C)         : 1 - {p_above_40:.4f} = {p_below_40:.4f} = {p_below_40*100:.2f}%  [Complement Rule]")
print(f"  P(T ≥ 45°C)         : {sum(1 for t in temperatures if t>=45)}/{n} = {p_above_45:.4f} = {p_above_45*100:.2f}%")
print(f"  P(40°C ≤ T ≤ 43°C)  : {sum(1 for t in temperatures if 40<=t<=43)}/{n} = {p_40_to_43:.4f} = {p_40_to_43*100:.2f}%")
print()
print(f"  ⚠ WARNING: There is a {p_above_40*100:.1f}% chance any June day exceeds 40°C!")
print(f"  ⚠ DANGER : {p_above_45*100:.1f}% chance of exceeding 45°C heat threshold!")
print()

# ============================================================
#   CHAPTER 8 — NORMAL DISTRIBUTION
# ============================================================
print("=" * 60)
print("   CHAPTER 8 — NORMAL DISTRIBUTION")
print("=" * 60)
print(f"  Since Mean ≈ Median ≈ Mode → X ~ N({mean:.2f}, {std_dev:.4f}²)")
print()

# Empirical Rule
print(f"  EMPIRICAL RULE (68 - 95 - 99.7):")
print(f"  μ ± 1σ : {mean-std_dev:.2f}°C  to  {mean+std_dev:.2f}°C  → ≈ 68% of days")
print(f"  μ ± 2σ : {mean-2*std_dev:.2f}°C  to  {mean+2*std_dev:.2f}°C  → ≈ 95% of days")
print(f"  μ ± 3σ : {mean-3*std_dev:.2f}°C  to  {mean+3*std_dev:.2f}°C  → ≈ 99.7% of days")
print()

# Normal probabilities
z_40  = (40 - mean) / std_dev
p_norm_above40 = 1 - stats.norm.cdf(40, mean, std_dev)
p_norm_above45 = 1 - stats.norm.cdf(45, mean, std_dev)
p_norm_37_43   = stats.norm.cdf(43, mean, std_dev) - stats.norm.cdf(37, mean, std_dev)

print(f"  NORMAL DISTRIBUTION PROBABILITIES (using z-table):")
print(f"  z(40°C) = (40 - {mean:.2f}) / {std_dev:.4f} = {z_40:.4f}")
print(f"  P(T > 40°C) = 1 - Φ({z_40:.4f}) = {p_norm_above40:.4f} = {p_norm_above40*100:.2f}%")
print()
print(f"  z(45°C) = (45 - {mean:.2f}) / {std_dev:.4f} = {z_45:.4f}")
print(f"  P(T > 45°C) = 1 - Φ({z_45:.4f}) = {p_norm_above45:.4f} = {p_norm_above45*100:.2f}%")
print()

# ============================================================
#   CHAPTER 8 — CONFIDENCE INTERVAL
# ============================================================
print("=" * 60)
print("   CHAPTER 8 — CONFIDENCE INTERVAL (95%)")
print("=" * 60)

z_star = 1.96
se     = std_dev / math.sqrt(n)
E      = z_star * se
ci_low = mean - E
ci_up  = mean + E

print(f"  Formula : CI = x̄ ± z* × (s / √n)")
print(f"  z*      : 1.96  (for 95% confidence)")
print(f"  SE      : s/√n = {std_dev:.4f}/√{n} = {se:.4f}°C")
print(f"  E       : z* × SE = 1.96 × {se:.4f} = {E:.4f}°C")
print()
print(f"  Lower   : {mean:.4f} - {E:.4f} = {ci_low:.4f}°C")
print(f"  Upper   : {mean:.4f} + {E:.4f} = {ci_up:.4f}°C")
print()
print(f"  ✔ 95% CI : ({ci_low:.2f}°C ,  {ci_up:.2f}°C)")
print(f"  → We are 95% confident the TRUE mean June temperature")
print(f"    in Lahore lies between {ci_low:.2f}°C and {ci_up:.2f}°C")
print()

# ============================================================
#   FINAL SUMMARY
# ============================================================
print("=" * 60)
print("   PROBABILITY PROGRESSION SUMMARY")
print("=" * 60)
bar_scale = 40
def bar(p): return "█" * int(p * bar_scale)

print(f"  P(Any day > 40°C)          {p_norm_above40*100:>6.2f}%  {bar(p_norm_above40)}")
print(f"  P(Any day > 45°C danger)   {p_norm_above45*100:>6.2f}%  {bar(p_norm_above45)}")
print(f"  P(Day in 40–43°C range)    {p_40_to_43*100:>6.2f}%  {bar(p_40_to_43)}")
print(f"  P(Day ≤ 40°C — cool)       {p_below_40*100:>6.2f}%  {bar(p_below_40)}")
print()
print("=" * 60)
print("   CONCLUSION")
print("=" * 60)
print(f"  • Mean June temperature in Lahore = {mean:.2f}°C")
print(f"  • {p_norm_above40*100:.1f}% probability any June day exceeds 40°C")
print(f"  • Only {p_norm_above45*100:.2f}% chance of extreme 45°C+ heat")
print(f"  • No statistical outliers detected in the dataset")
print(f"  • 95% CI confirms true mean is between {ci_low:.2f}°C–{ci_up:.2f}°C")
print(f"  • This proves WHY heat alerts & water plans are needed")
print(f"    throughout ALL of June — not just some days!")
print("=" * 60)

# ============================================================
#   GRAPHS — 6 Charts saved as images
# ============================================================
print()
print("  Generating graphs...")

# ── Graph 1: Line Chart ───────────────────────────────────────
fig, ax = plt.subplots(figsize=(11, 5))
ax.plot(range(1,31), temperatures, color='#E63946', linewidth=2.5,
        marker='o', markersize=5, markerfacecolor='#FF6B6B', label='Daily Max Temp')
ax.axhline(mean, color='#2196F3', linewidth=1.8, linestyle='--', label=f'Mean = {mean:.2f}°C')
ax.axhline(45, color='#FF6F00', linewidth=1.5, linestyle=':', label='Danger Level (45°C)')
ax.fill_between(range(1,31), temperatures, mean,
                where=[t > mean for t in temperatures], alpha=0.15, color='#E63946')
ax.fill_between(range(1,31), temperatures, mean,
                where=[t <= mean for t in temperatures], alpha=0.15, color='#2196F3')
ax.set_title('Daily Maximum Temperature — Lahore, June 2024', fontsize=14, fontweight='bold')
ax.set_xlabel('Day of June', fontsize=12)
ax.set_ylabel('Temperature (°C)', fontsize=12)
ax.set_xticks(range(1,31))
ax.set_ylim(34, 50)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3, linestyle='--')
plt.tight_layout()
plt.savefig('graph1_temperature_trend.png', dpi=150, bbox_inches='tight')
plt.close()

# ── Graph 2: Histogram ────────────────────────────────────────
colors_hist = ['#4CAF50','#2196F3','#FF9800','#E63946','#9C27B0']
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(class_names, freqs, color=colors_hist, edgecolor='black', linewidth=0.8, width=0.75)
for bar_obj, freq in zip(bars, freqs):
    ax.text(bar_obj.get_x() + bar_obj.get_width()/2, bar_obj.get_height()+0.1,
            str(freq), ha='center', va='bottom', fontweight='bold', fontsize=12)
ax.set_title('Frequency Histogram — June Temperature Classes', fontsize=14, fontweight='bold')
ax.set_xlabel('Temperature Class (°C)', fontsize=12)
ax.set_ylabel('Frequency (Number of Days)', fontsize=12)
ax.set_ylim(0, max(freqs) + 3)
ax.grid(True, axis='y', alpha=0.3, linestyle='--')
plt.tight_layout()
plt.savefig('graph2_histogram.png', dpi=150, bbox_inches='tight')
plt.close()

# ── Graph 3: Normal Distribution ─────────────────────────────
x_range = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 500)
y_norm  = stats.norm.pdf(x_range, mean, std_dev)
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x_range, y_norm, color='#1565C0', linewidth=2.5,
        label=f'N(μ={mean:.2f}, σ={std_dev:.2f})')
x_s1 = np.linspace(40, mean+4*std_dev, 300)
ax.fill_between(x_s1, stats.norm.pdf(x_s1, mean, std_dev),
                alpha=0.35, color='#E63946', label=f'P(T>40°C) = {p_norm_above40:.4f}')
x_s2 = np.linspace(45, mean+4*std_dev, 300)
ax.fill_between(x_s2, stats.norm.pdf(x_s2, mean, std_dev),
                alpha=0.6, color='#FF6F00', label=f'P(T>45°C) = {p_norm_above45:.4f}')
ax.axvline(mean, color='#1565C0', linestyle='--', linewidth=1.5, label=f'Mean={mean:.2f}°C')
for k, col in [(1,'#4CAF50'),(2,'#FF9800'),(3,'#9C27B0')]:
    ax.axvline(mean+k*std_dev, color=col, linestyle=':', linewidth=1)
    ax.axvline(mean-k*std_dev, color=col, linestyle=':', linewidth=1)
ax.set_title('Normal Distribution — June Temperature Probabilities', fontsize=14, fontweight='bold')
ax.set_xlabel('Temperature (°C)', fontsize=12)
ax.set_ylabel('Probability Density', fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.25, linestyle='--')
plt.tight_layout()
plt.savefig('graph3_normal_distribution.png', dpi=150, bbox_inches='tight')
plt.close()

# ── Graph 4: Box Plot ─────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 5))
bp = ax.boxplot(temperatures, vert=True, patch_artist=True, widths=0.5,
                medianprops=dict(color='#E63946', linewidth=2.5),
                boxprops=dict(facecolor='#64B5F6', color='#1565C0'),
                whiskerprops=dict(color='#1565C0', linewidth=1.5),
                capprops=dict(color='#1565C0', linewidth=2),
                flierprops=dict(marker='o', color='#E63946', markersize=8))
ax.set_title('Box Plot — Five Number Summary\n(No Outliers Detected)', fontsize=13, fontweight='bold')
ax.set_ylabel('Temperature (°C)', fontsize=12)
ax.set_xticks([1])
ax.set_xticklabels(['June 2024 Lahore'])
for val, lbl in zip(
    [min(temperatures), q1, median, q3, max(temperatures)],
    [f'Min={min(temperatures)}°C', f'Q1={q1}°C', f'Median={median}°C',
     f'Q3={q3}°C', f'Max={max(temperatures)}°C']
):
    ax.annotate(lbl, xy=(1.28, val), fontsize=9, color='#1A237E', va='center')
ax.set_xlim(0.5, 1.9)
ax.grid(True, axis='y', alpha=0.3, linestyle='--')
plt.tight_layout()
plt.savefig('graph4_boxplot.png', dpi=150, bbox_inches='tight')
plt.close()

# ── Graph 5: Pie Chart ────────────────────────────────────────
cat_labels = ['Moderate\n37–39°C','Hot\n40–42°C','Very Hot\n43–45°C','Extreme\n46°C+']
cat_counts = [
    sum(1 for t in temperatures if 37<=t<=39),
    sum(1 for t in temperatures if 40<=t<=42),
    sum(1 for t in temperatures if 43<=t<=45),
    sum(1 for t in temperatures if t>=46),
]
pie_colors = ['#4CAF50','#FF9800','#E63946','#9C27B0']
fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(
    cat_counts, labels=cat_labels, colors=pie_colors,
    autopct='%1.1f%%', startangle=140, explode=(0.04,0.04,0.04,0.08),
    pctdistance=0.75, textprops={'fontsize': 10})
for at in autotexts:
    at.set_fontweight('bold')
    at.set_fontsize(11)
ax.set_title('Temperature Category Distribution — June Lahore', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('graph5_pie_chart.png', dpi=150, bbox_inches='tight')
plt.close()

# ── Graph 6: Probability Bar Chart ───────────────────────────
prob_labels = ['P(T > 40°C)', 'P(T > 45°C)\nDanger!', 'P(40≤T≤43°C)', 'P(T ≤ 40°C)\nCool Day']
prob_values = [p_norm_above40*100, p_norm_above45*100, p_40_to_43*100, p_below_40*100]
prob_colors = ['#E63946', '#FF6F00', '#2196F3', '#4CAF50']
fig, ax = plt.subplots(figsize=(9, 5))
bars2 = ax.bar(prob_labels, prob_values, color=prob_colors, edgecolor='black', linewidth=0.8, width=0.55)
for b, v in zip(bars2, prob_values):
    ax.text(b.get_x() + b.get_width()/2, b.get_height()+0.5,
            f'{v:.2f}%', ha='center', va='bottom', fontweight='bold', fontsize=11)
ax.set_title('Probability of Heat Events — Lahore June (Normal Distribution)', fontsize=13, fontweight='bold')
ax.set_ylabel('Probability (%)', fontsize=12)
ax.set_ylim(0, 100)
ax.axhline(50, color='gray', linestyle='--', linewidth=1, alpha=0.5)
ax.grid(True, axis='y', alpha=0.3, linestyle='--')
plt.tight_layout()
plt.savefig('graph6_probabilities.png', dpi=150, bbox_inches='tight')
plt.close()

print("  ✅ All 6 graphs saved successfully!")
print()
print("  Graphs saved:")
print("   graph1_temperature_trend.png")
print("   graph2_histogram.png")
print("   graph3_normal_distribution.png")
print("   graph4_boxplot.png")
print("   graph5_pie_chart.png")
print("   graph6_probabilities.png")
print()
print("=" * 60)
print("   Thank You Sir: Fakhar Mustafa")
print("   Student: Alisha Sultan ")
print("   COMSATS University ")
print("=" * 60)
