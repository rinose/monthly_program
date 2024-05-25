# Input month name. 
# Output: create pdf with two columns, First column, 120px with, contains monthly days in format day number and day name, while second column contains an empty text.

import os
import sys
import calendar
from fpdf import FPDF
import locale
import datetime

os.environ['LANG'] = 'it_IT.UTF-8'
locale.setlocale(locale.LC_TIME, 'it_IT.UTF-8')


def create_pdf(month):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.set_left_margin(5)
    pdf.set_right_margin(5)
    pdf.set_top_margin(10)
    pdf.set_font("Arial", size=12)
    pdf.set_fill_color(200, 220, 255)
    pdf.set_text_color(0)
    pdf.set_draw_color(0)
    pdf.set_line_width(0.3)
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"Month of {month}", 0, 1, "C")
    pdf.set_font("Arial", "B", 12)
    pdf.ln(10)
    pdf.set_fill_color(200, 220, 255)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(30, 10, "Day", 1, 0, "C", 1)
    pdf.cell(160, 10, "Notes", 1, 1, "C", 1)
    pdf.set_fill_color(255, 255, 255)
    pdf.set_font("Arial", size=12)
    # set calendar in italian language
    calendar.setfirstweekday(6)

    # get current year
    year = datetime.datetime.now().year

    for i in range(1, calendar.monthrange(year, list(calendar.month_name).index(month))[1] + 1):
        pdf.cell(30, 10, f"{i} {calendar.day_name[calendar.weekday(year, list(calendar.month_name).index(month), i)].capitalize()}", 1, 0, "L")
        pdf.cell(160, 10, "", 1, 1, "C")
    pdf.output(f"{month}.pdf")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        create_pdf(sys.argv[1])
    else:
        print("Usage: python dopdf.py <month>")
        sys.exit(1)

# Usage: python dopdf.py <month>
# Example: python dopdf.py giugno

