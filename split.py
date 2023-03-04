import pandas as pd
import datetime

try:
    X = input("Whats the name of the file that you want to convert? (include the .csv at the end) ")

    Y = input("Whats the name of the relevant column? (watch out for lower- and upper-case) ")

    df = pd.read_csv(X)

    df.columns = [col.lower() for col in df.columns]

    #df.columns = str.lower()

    options = df[Y].unique()

    start = 0
    list_names = []
    for i in options:
        name = f"Convert{start}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
        temp = df[df[Y] == options[start]]
        #exec(f"{name} = df[df[Y] == options[start]]")
        temp.to_excel(f"{name}.xlsx", index=False)
        print(f"{name}.xlsx successfully saved")
        start = start + 1

    #meal_plan_1 = df[df["type_of_meal_plan"] == "Meal Plan 1"]

except:
    print("ERROR")


#if __name__ == '__main__':
#    run_convert
