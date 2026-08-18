# Automated Daily Status Reporting System

A Python-based automation project that transforms project activity data into a structured status report and prepares a ready-to-review Microsoft Outlook email draft.

The project demonstrates how repetitive project reporting tasks can be automated while keeping the final review and email sending under user control.

---

## Project Overview

Preparing a daily project status report can involve several repetitive tasks:

- Reviewing the activity tracker
- Checking planned finish dates
- Identifying delayed activities
- Finding upcoming deadlines
- Reviewing high-priority open items
- Preparing a management summary
- Drafting the status email
- Attaching the latest report

This project combines those steps into one Python workflow.

```text
Project Tracker
      ↓
Python Data Processing
      ↓
Status Analysis
      ↓
Excel Management Report
      ↓
Email Summary
      ↓
Outlook Draft + Attachment
      ↓
User Review and Send
```

---

## Input: Project Activity Tracker

The automation reads an Excel-based project tracker containing activity information such as planned dates, actual dates, status, progress, priority, ownership, and remarks.

![Project Tracker](screenshots/project-tracker.png)

The portfolio version uses synthetic project data and does not contain confidential company, client, or operational information.

---

## Automated Status Analysis

Python evaluates the tracker using the selected report date and identifies:

| Indicator | Description |
|---|---|
| Total Activities | All activities included in the tracker |
| Completed | Activities marked as completed |
| In Progress | Activities currently being worked on |
| Delayed | Open activities beyond their planned finish date |
| Due Within 3 Days | Open activities approaching their planned finish date |
| Critical Open Items | High-priority activities that remain open |

The project includes a Demo Mode with a fixed report date so the portfolio dataset produces consistent results when the program is run in the future.

For actual use, Demo Mode can be disabled so the analysis uses the current date.

---

## Generated Excel Report

The program automatically creates a formatted Excel report containing a management-level summary and detailed activity lists.

![Automated Status Dashboard](screenshots/summary-dashboard.png)

The generated workbook contains four worksheets:

- Summary
- Delayed
- Due Soon
- Critical

The Summary sheet provides a quick view of the overall project status, while the supporting worksheets contain the activities behind each indicator.

---

## Outlook Email Automation

After generating the report, the program prepares a Microsoft Outlook email draft.

![Outlook Draft](screenshots/outlook-draft.png)

The draft automatically includes:

- Report date
- Current activity status summary
- Delayed activity count
- Due-soon activity count
- Critical open item count
- Up to five delayed activities requiring attention
- Generated Excel report as an attachment

The email is intentionally opened as a draft instead of being sent automatically, allowing the user to review the report before sending it.

---

## Key Features

- Excel project tracker import
- Automated date-based activity analysis
- Delayed activity detection
- Upcoming deadline monitoring
- High-priority open item identification
- Automated Excel report generation
- Management-style KPI summary
- Separate exception reports
- HTML email generation
- Automatic Outlook draft creation
- Automatic report attachment
- Demo and live reporting modes
- Manual review before email sending

---

## Technologies Used

- Python
- Pandas
- OpenPyXL
- PyWin32
- Microsoft Excel
- Microsoft Outlook

---

## Project Structure

```text
Automated-Email-Reporting/
│
├── data/
│   └── project_tracker.xlsx
│
├── output/
│   └── daily_status_report.xlsx
│
├── screenshots/
│   ├── project-tracker.png
│   ├── summary-dashboard.png
│   └── outlook-draft.png
│
├── src/
│   ├── analyze_tracker.py
│   ├── generate_report.py
│   └── create_email.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Running the Project

Create and activate a Python virtual environment, then install the required packages:

```bash
pip install -r requirements.txt
```

Run the automation:

```bash
python main.py
```

The program will:

1. Load the project tracker
2. Analyze activity status
3. Generate the Excel status report
4. Prepare the email summary
5. Attach the generated report
6. Open the Outlook draft for review

---

## Demo Mode

The portfolio version uses:

```python
DEMO_MODE = True
DEMO_REPORT_DATE = "2026-08-18"
```

This keeps the demonstration results consistent regardless of when the repository is reviewed.

For live reporting:

```python
DEMO_MODE = False
```

The program will then use the current date.

---

## Possible Future Improvements

Potential enhancements include:

- Project-specific filtering
- Configurable due-date thresholds
- Recipient configuration
- Historical reporting
- Trend charts
- Automated run logs
- Multiple-project summaries
- User interface for non-technical users

---

## Author

Regina Grace

Mechanical Engineering • Project Controls • Data & Automation