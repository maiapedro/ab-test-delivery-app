import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import levene, ttest_ind
from pathlib import Path

# Load dataset
file_path = Path(__file__).resolve().parent / "ab_test.csv"
df = pd.read_csv(file_path)

# Calculate the 99th percentiles
order_limit = np.percentile(df["order_value"], 99)
duration_limit = np.percentile(df["session_duration"], 99)

# Remove outliers
df_clean = df[
    (df["order_value"] <= order_limit) &
    (df["session_duration"] <= duration_limit)
].copy()

# Apply log transformation
df_clean["log_order_value"] = np.log(df_clean["order_value"])

# Plot histogram with 30 bins
df_clean.hist(column="log_order_value", bins=30)
plt.show()

# Separate control and experimental groups
control = df_clean[
    df_clean["group"] == "Control"
]["log_order_value"]

experimental = df_clean[
    df_clean["group"] == "Experimental"
]["log_order_value"]

# Levene's test
w_stat, p_levene = levene(control, experimental)

equal_variances = p_levene > 0.05

print("Levene's test")
print(f"W = {w_stat:.3f}, p-value {'> 0.05' if equal_variances else '<= 0.05'}")
print(f"Reject null hypothesis: {'no' if equal_variances else 'yes'}")
print(f"Variances are equal: {'yes' if equal_variances else 'no'}")

print()

# Independent samples t-test
t_stat, p_ttest = ttest_ind(
    control,
    experimental,
    equal_var=equal_variances
)

equal_means = p_ttest > 0.05

print("T-test")
print(f"t = {t_stat:.3f}, p-value {'> 0.05' if equal_means else '<= 0.05'}")
print(f"Reject null hypothesis: {'no' if equal_means else 'yes'}")
print(f"Means are equal: {'yes' if equal_means else 'no'}")
