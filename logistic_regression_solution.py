import pandas as pd
from sklearn.linear_model import LogisticRegression


# ======================================================================
print("...1...")
# ======================================================================


df = pd.read_csv("dataset.csv")


print("\n--- PRVNÍCH 5 ŘÁDKŮ NAČTENÉHO DATASETU ---")
print(df.head(5))


print("\n--- ZÁKLADNÍ INFORMACE (INFO) ---")
df.info()


pocet_radku = df.shape[0]
pocet_sloupcu = df.shape[1]
print(f"Dataset má v původním stavu {pocet_radku} řádků a {pocet_sloupcu} sloupců.")




# ======================================================================
print("...2...")
# ======================================================================


# Převedeme textové anomálie ('?', 'invalid') ve sloupcích na skutečné NaN
columns_to_numeric = ['study_hours', 'sleep_hours', 'attendance', 'previous_score', 'coffee_cups', 'final_score']
for col in columns_to_numeric:
   df[col] = pd.to_numeric(df[col], errors='coerce')


# Nahrazení chybějících hodnot (NaN) mediánem pro nezávislé proměnné
features_to_impute = ['study_hours', 'sleep_hours', 'attendance', 'previous_score', 'coffee_cups']
for col in features_to_impute:
   median_value = df[col].median()
   df[col] = df[col].fillna(median_value)


# Odstranění řádku, kde chybí cílová proměnná (final_score u studenta ID 11)
df = df.dropna(subset=['final_score'])


# Omezení nesmyslných hodnot (např. ořezání docházky do rozmezí 0 až 100)
df['attendance'] = df['attendance'].clip(lower=0, upper=100)


# Odstranění duplicit na základě unikátního student_id
df = df.drop_duplicates(subset=['student_id'])


# Změna datových typů na správné (optimální) formáty
df['student_id'] = df['student_id'].astype(int)
df['study_hours'] = df['study_hours'].astype(float)
df['sleep_hours'] = df['sleep_hours'].astype(float)
df['attendance'] = df['attendance'].astype(int)
df['previous_score'] = df['previous_score'].astype(int)
df['coffee_cups'] = df['coffee_cups'].astype(int)
df['final_score'] = df['final_score'].astype(int)


print("\n--- DATASET PO VYČIŠTĚNÍ ---")
print(df)




# ======================================================================
print("...3...")
# ======================================================================


df['passed'] = (df['final_score'] >= 75).astype(int)


print("\n--- UKÁZKA DATASETU S KATEGORIÍ 'passed' ---")
print(df[['student_id', 'final_score', 'passed']])




# ======================================================================
print("...4...")
# ======================================================================


srovnani_skupin = df.groupby('passed')[['study_hours', 'sleep_hours', 'attendance', 'previous_score', 'coffee_cups', 'final_score']].mean()


print("\n--- PRŮMĚRNÉ HODNOTY PODLE ÚSPĚŠNOSTI ---")
print(srovnani_skupin.round(2))




# ======================================================================print(“...5...")
# ======================================================================


# Definice vstupních vlastností (X) a cíle (y)
X = df[['study_hours', 'sleep_hours', 'attendance', 'previous_score', 'coffee_cups']]
y = df['passed']


# Inicializace a natrénování modelu
model = LogisticRegression()
model.fit(X, y)


print("Model byl úspěšně natrénován.")




# ======================================================================
print("...6...")
# ======================================================================


# Získání finální předpovědi (0 nebo 1)
df['predicted_passed'] = model.predict(X)


# Získání konkrétní pravděpodobnosti pro třídu 1 (úspěch)
df['probability_passed'] = model.predict_proba(X)[:, 1]


print("\n--- MATRICE PREDIKCÍ A PRAVDĚPODOBNOSTÍ ---")
print(df[['student_id', 'passed', 'predicted_passed', 'probability_passed']])




# ======================================================================
print("...7...")
# ======================================================================


# Výpočet přesnosti porovnáním shody
accuracy = (df['predicted_passed'] == df['passed']).mean()
df['chyba'] = df['passed'] != df['predicted_passed']


print(f"Accuracy modelu je: {accuracy * 100:.1f} %")


print("\n--- DETEKCE CHYB V PREDIKCÍCH ---")
print(df[['student_id', 'passed', 'predicted_passed', 'chyba']])




# ======================================================================
print("...8...")
# ======================================================================


print(f"Absolutní člen (Intercept): {model.intercept_[0]:.4f}")
for sloupec, koeficient in zip(X.columns, model.coef_[0]):
   print(f"Vliv sloupce '{sloupec}': {koeficient:.4f}")



