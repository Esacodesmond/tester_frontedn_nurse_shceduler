import streamlit as st

import pandas as pd
import numpy as np

st.title("🎈 My new app")

# Data
# num_nurses = 17
# all_nurses = range(num_nurses)
class Nurse:
    def __init__(self, name, rank, line, cumulativeDO=0, cumulativeN=0):
        self.name = name
        self.rank = rank
        self.line = line
        self.cumulativeDO = cumulativeDO
        self.cumulativeN = cumulativeN

    def __str__(self):
        return f"Nurse {self.name}"

# Define the nurse data
all_nurses = [
    Nurse(name='Nurse1', rank='RN', line=1),
    Nurse(name='Nurse2', rank='RN', line=1),
    Nurse(name='Nurse3', rank='EN', line=1),
    Nurse(name='Nurse4', rank='EN', line=1),
    Nurse(name='Nurse5', rank='RN', line=1),
    Nurse(name='Nurse6', rank='EN', line=1),
    Nurse(name='Nurse7', rank='RN', line=1),
    Nurse(name='Nurse8', rank='EN', line=1),

    Nurse(name='Nurse9', rank='EN', line=2),
    Nurse(name='Nurse10', rank='RN', line=2),
    Nurse(name='Nurse11', rank='EN', line=2),
    Nurse(name='Nurse12', rank='RN', line=2),
    Nurse(name='Nurse13', rank='EN', line=2),
    Nurse(name='Nurse14', rank='RN', line=2),
    Nurse(name='Nurse15', rank='EN', line=2),
    Nurse(name='Nurse16', rank='RN', line=2),

    Nurse(name='Nurse17', rank='RN', line=3),
    Nurse(name='Nurse18', rank='EN', line=3),
    Nurse(name='Nurse19', rank='RN', line=3),
    Nurse(name='Nurse20', rank='EN', line=3),
    Nurse(name='Nurse21', rank='RN', line=3),
    Nurse(name='Nurse22', rank='EN', line=3),
    Nurse(name='Nurse23', rank='RN', line=3),
    Nurse(name='Nurse24', rank='EN', line=3),

    Nurse(name='Nurse25', rank='RN', line=4),
    Nurse(name='Nurse26', rank='EN', line=4),
    Nurse(name='Nurse27', rank='RN', line=4),
    Nurse(name='Nurse28', rank='EN', line=4),
    Nurse(name='Nurse29', rank='RN', line=4),
    Nurse(name='Nurse30', rank='EN', line=4),
    Nurse(name='Nurse31', rank='RN', line=4),



]

# Convert the list of Nurse objects into a DataFrame
nurse_df = pd.DataFrame([{
    'Name': nurse.name,
    'Rank': nurse.rank,
    'Line': nurse.line
} for nurse in all_nurses])


# Initialize an empty DataFrame for the schedule
schedule_df = pd.DataFrame(columns=['Name', 'Rank', 'Line'] + [str(date.date()) for date in schedule_dates])

# Populate the schedule DataFrame with nurse data
for index, row in nurse_df.iterrows():
    # Create a dictionary for the row
    new_row = {
        'Name': row['Name'],
        'Rank': row['Rank'],
        'Line': row['Line'],
        **{str(date.date()): '' for date in schedule_dates}  # Initialize shifts with empty strings
    }

    # Use pd.concat to add the new row to the DataFrame
    schedule_df = pd.concat([schedule_df, pd.DataFrame([new_row])], ignore_index=True)

print(schedule_df)
