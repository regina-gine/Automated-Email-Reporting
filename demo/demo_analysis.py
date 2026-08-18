from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent

DATA_FILE = (
    BASE_DIR
    / "sample_data"
    / "project_tracker_demo.csv"
)

REPORT_DATE = pd.Timestamp("2026-08-18")


def load_data():
    df = pd.read_csv(
        DATA_FILE,
        parse_dates=["Planned_Finish"]
    )

    return df


def analyze_status(df):

    df["Days_To_Due"] = (
        df["Planned_Finish"] - REPORT_DATE
    ).dt.days

    df["Delayed"] = (
        (df["Status"] != "Completed")
        & (df["Planned_Finish"] < REPORT_DATE)
    )

    df["Due_Soon"] = (
        (df["Status"] != "Completed")
        & (df["Days_To_Due"] >= 0)
        & (df["Days_To_Due"] <= 3)
    )

    df["Critical_Open"] = (
        (df["Priority"] == "High")
        & (df["Status"] != "Completed")
    )

    summary = {
        "Total Activities": len(df),
        "Completed": int(
            (df["Status"] == "Completed").sum()
        ),
        "In Progress": int(
            (df["Status"] == "In Progress").sum()
        ),
        "Delayed": int(
            df["Delayed"].sum()
        ),
        "Due Within 3 Days": int(
            df["Due_Soon"].sum()
        ),
        "Critical Open Items": int(
            df["Critical_Open"].sum()
        ),
    }

    return df, summary


def show_summary(summary):

    print()
    print("DAILY PROJECT STATUS - DEMO")
    print("=" * 34)
    print(
        f"Report Date: "
        f"{REPORT_DATE.strftime('%d-%b-%Y')}"
    )
    print()

    for metric, value in summary.items():
        print(f"{metric:<22} {value}")


def show_attention_items(df):

    attention = (
        df[df["Delayed"]]
        .sort_values(
            by=[
                "Priority",
                "Planned_Finish",
            ],
            ascending=[
                True,
                True,
            ],
        )
        .head(5)
    )

    print()
    print("ITEMS REQUIRING ATTENTION")
    print("=" * 34)

    if attention.empty:
        print("No delayed activities.")
        return

    for _, row in attention.iterrows():

        finish_date = (
            row["Planned_Finish"]
            .strftime("%d-%b-%Y")
        )

        print(
            f"{row['Activity_ID']} | "
            f"{row['Activity']} | "
            f"{finish_date} | "
            f"{row['Priority']}"
        )


def main():

    print("Loading demonstration project data...")

    df = load_data()

    analyzed_df, summary = analyze_status(df)

    show_summary(summary)

    show_attention_items(
        analyzed_df
    )

    print()
    print(
        "Demo complete. "
        "The portfolio version demonstrates "
        "the core status-analysis logic only."
    )


if __name__ == "__main__":
    main()