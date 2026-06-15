import pandas as pd
from sklearn.linear_model import LinearRegression


# =====================================================================
print("...1...")
# =====================================================================


# Načtení dat (znovu pro čistý start)
df = pd.read_csv('dataset.csv')


# Zobrazení prvních 5 řádků
print("\nPrvních 5 řádků surových dat:")
print(df.head(5))


# Zobrazení základních informací
print("\nZákladní informace o datasetu:")
df.info()


# Počet řádků a sloupců
print(f"\nPůvodní rozměry datasetu (řádky, sloupce): {df.shape}")




# =====================================================================
print("...2...")
# =====================================================================


# 1. Převod textových chyb (?, invalid, NaN jako text) na skutečné NaN
numeric_cols = ['study_hours', 'sleep_hours', 'attendance', 'previous_score', 'coffee_cups', 'final_score']
for col in numeric_cols:
   df[col] = pd.to_numeric(df[col], errors='coerce')


# 2. Odstranění řádků s chybějící cílovou proměnnou (final_score)
df = df.dropna(subset=['final_score'])


# 3. Nahrazení chybějících hodnot v ostatních sloupcích pomocí mediánu
for col in ['study_hours', 'sleep_hours', 'attendance', 'previous_score', 'coffee_cups']:
   median_value = df[col].median()
   df[col] = df[col].fillna(median_value)


# 4. Odstranění duplicit (pokud by se vyskytovaly)
df = df.drop_duplicates()


# 5. Převod vybraných sloupců na celá čísla pro lepší čitelnost
int_cols = ['study_hours', 'attendance', 'previous_score', 'coffee_cups', 'final_score']
df[int_cols] = df[int_cols].astype(int)


print("\nVyčištěný dataset připravený k analýze:")
print(df.to_string(index=False))




# =====================================================================
print("...3...")
# =====================================================================


correlation_study = df['study_hours'].corr(df['final_score'])
correlation_sleep = df['sleep_hours'].corr(df['final_score'])


print(f"Korelace (study_hours vs final_score): {correlation_study:.4f}")
print(f"Korelace (sleep_hours vs final_score): {correlation_sleep:.4f}")




# =====================================================================
print("...4...")
# =====================================================================


correlation_attendance = df['attendance'].corr(df['final_score'])
print(f"Korelace (attendance vs final_score): {correlation_attendance:.4f}")


# Rozdělení studentů podle průměrné docházky (cca 83 %)
low_attendance = df[df['attendance'] < 83]
high_attendance = df[df['attendance'] >= 83]


print(f"Průměrné skóre studentů s NÍZKOU docházkou (< 83 %): {low_attendance['final_score'].mean():.1f}")
print(f"Průměrné skóre studentů s VYSOKOU docházkou (>= 83 %): {high_attendance['final_score'].mean():.1f}")




# =====================================================================
print("...5...")
# =====================================================================


correlation_coffee = df['coffee_cups'].corr(df['final_score'])
print(f"Korelace (coffee_cups vs final_score): {correlation_coffee:.4f}")




# =====================================================================
print("...6...")
# =====================================================================


# Výpočet korelace všech číselných sloupců vůči výsledku (bez student_id)
correlation_matrix = df.drop(columns=['student_id']).corr()
print("\nSeřazené korelace všech veličin vůči final_score:")
print(correlation_matrix['final_score'].sort_values(ascending=False))




# =====================================================================
print("...7...")
# =====================================================================


# Výběr vstupních (X) a výstupní (y) proměnné
X = df[['study_hours', 'sleep_hours', 'attendance', 'previous_score', 'coffee_cups']]
y = df['final_score']


# Inicializace a natrénování modelu
model = LinearRegression()
model.fit(X, y)


# Výpočet predikcí a určení chyby
df['predicted_score'] = model.predict(X)
df['residual_error'] = df['final_score'] - df['predicted_score']


print("\nSrovnání skutečného výsledku s predikcí modelu:")
print(df[['student_id', 'final_score', 'predicted_score', 'residual_error']].to_string(index=False))


# Výpočet celkové úspěšnosti modelu (R^2 koeficient)
r2_score = model.score(X, y)
print(f"\nCelková přesnost modelu (R^2 koeficient): {r2_score:.4f}")




# =====================================================================
print("...8...")
# =====================================================================


coefficients = pd.Series(model.coef_, index=X.columns)
print(f"Základní konstanta modelu (intercept): {model.intercept_:.4f}")
print("\nVáhy jednotlivých proměnných v regresní rovnici:")
print(coefficients.sort_values(ascending=False).to_string())



