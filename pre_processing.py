import csv
import pandas as pd


def pre_process():
    df = pd.read_csv("created_dataset/dubawa_dataset.csv")



    # df = df.drop(columns=["Link"])

    print(df.head())

    for index, row in df.iterrows():

        print(f"Index: {index}")
        title = row["Title"].lower()

        if "true" in title:
            row["Label"] = 1
            row["Title"] = title.replace("true", "")
            if row["Title"].startswith("!"):
                row["Title"] = title.replace("!", "")
            row["Title"] = row["Title"].strip()
        elif "false" in title:
            row["Label"] = 0
            row["Title"] = title.replace("false", "")
        elif "misleading" in title:
            row["Label"] = 0
            row["Title"] = title.replace("misleading", "")
        
        print(f"\tTitle: {title}")

        content = row["Content"].lower()

        if "true" in content:
            row["Label"] = 1
            row["Content"] = content.replace("true", "")
        elif "false" in content:
            row["Label"] = 0
            row["Content"] = content.replace("false", "")
        elif "misleading" in content:
            row["Label"] = 0
            row["Content"] = content.replace("misleading", "")
        row["Content"] = content.replace("claim:", "")

        if type(row["Label"]) != int and type(row["Label"]) != float:
            label = row["Label"].lower()

            if "true" in label:
                row["Label"] = 1
            elif "false" in label:
                row["Label"] = 0
            elif "misleading" in label:
                row["Label"] = 0
            

        print(f"\tContent: {row["Content"]}")
        print(f"Label: {row["Label"]}")

    df.to_csv("created_dataset/pre_processed.csv", index=False)


def drop_columns():

    df = pd.read_csv("created_dataset/pre_processed.csv")

    df = df.drop(columns=["Link", "Title"])
    df = df[["Content", "Label"]]
    df = df.dropna()
    df["Label"] = df["Label"].astype(int)

    df.to_csv("created_dataset/final_dataset.csv", index=False)

    print(df.head())

if __name__ == "__main__":

    drop_columns()
    