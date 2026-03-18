import pandas as pd

print("📊 CSV ANALYZER TOOL")

file_path = input('Enter the CSV Datset: ')

try:
    df = pd.read_csv(file_path)
    print("\n✅ File loaded successfully!")
except:
    print("\n❌ Error loading file. Check path.")
    exit()

df = df.dropna()
df = df.fillna(0)

while True:
    print("\n Choose an Option: ")
    print("1. Views First rows")
    print("2. Dataset info")
    print("3. Statistics")
    print("4. Missing Value")
    print("5. Duplicate rows")
    print("6. Column names")
    print("7. Remove Duplicate Rows")
    print("8. Fill Missing Value")
    print("9. Drop Missing Value")
    print("10. Rename a Colummn")
    print("11. Save cleaned CSV")
    print("12. Exit")

    choice = input("Enter Option: ")

    if choice == '1':
        print('First 5 Rows: ')
        print(df.head())

    elif choice == '2':
        print('Dataset Info: ')
        print(df.info())

    elif choice == '3':
        print('Statistical Analysis: ')
        print(df.describe())

    elif choice == '4':
        print('Missing Value: ')
        print(df.isnull().sum())

    elif choice == '5':
        print('Duplicate Rows: ')
        print(df.duplicated().sum())

    elif choice == '6':
        print('Columns')
        print(df.columns.tolist())
    
    elif choice == '7':
        print('Remove Duplicate Rows')
        before = df.shape[0]
        df = df.drop_duplicates()
        after = df.shape[0]
        print(f"\n✅ Removed {before - after} duplicate rows.")
        
    elif choice == '8':
        print('Fill Missing Value')
        value = input("Enter value to fill missing data: ")
        df = df.fillna(value)
        print("\n✅ Missing values filled.")

    elif choice == '9':
        print('Drop Missing Value')
        before = df.shape[0]
        df = df.dropna()
        after = df.shape[0]
        print(f"\n✅ Dropped {before - after} rows with missing values.")

    elif choice == '10':
        print('Rename a Colummn')
        print("Columns:", df.columns.tolist())
        old = input("Enter column name to rename: ")
        new = input("Enter new column name: ")
        df = df.rename(columns={old: new})
        print("\n✅ Column renamed successfully.")


    elif choice == '11':
        print('Save cleaned CSV')
        save_path = input("Enter filename to save cleaned CSV: ")
        df.to_csv(save_path, index=False)
        print(f"\n✅ Cleaned file saved as {save_path}")

    elif choice == '12':
        break
    
    else:
        print("Invalid Choice")