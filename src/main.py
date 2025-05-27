from comparetoavg import compareToAvg

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))
    avg = (num1 + num2 + num3) / 3
    compareToAvg(avg, [num1, num2, num3])

if __name__ == "__main__":
    main()
import sqlite3

def save_df_to_sql(df, db_name="question2_data.db", table_name="merged_data"):
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
    print(f"Data saved to {db_name} in table '{table_name}'.")

# Call the function with your merged dataframe
save_df_to_sql(DF3)

