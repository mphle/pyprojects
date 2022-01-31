#Imports
from fpdf import FPDF
import subprocess
import webbrowser

#Classes
class Bill():
    """
    Object cointaining data about a bill, such as
    total amount and period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate():
    """
    Contains a flatmate - person who lives in the flat
    and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, other_flatmate, precision=2):
        weight = self.days_in_house / (self.days_in_house + other_flatmate.days_in_house)
        to_pay = weight * bill.amount
        return round(to_pay,precision)


class PdfReport():
    """
    Creates a Pdf file that contains data about the flatmates,
    such as their names, their due amounts, and the period
    of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # insert icon
        pdf.image("house.png", w=30, h=30)

        # insert title
        pdf.set_font(family="Times", style="B", size=24)
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # insert period label and value
        pdf.set_font(family="Times", style="B", size=14)
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # insert name and due amount of the first flatmate
        pdf.set_font(family="Times", size=12)

        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=str(flatmate1.pays(bill, flatmate2)), border=0, ln=1)

        # insert name and due amount of the second flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=str(flatmate2.pays(bill, flatmate1)), border=0)

        pdf.output(self.filename)

        subprocess.Popen(self.filename, shell=True)


#User input
amount = float(input("Hey user, enter the bill amount: "))
period = input("Now enter the bill period (Eg December 2020): ")

f1 = input("Whats the name of the first flatmate? ")
f1d = int(input(f"How many days was {f1} in the house during the bill period? "))

f2 = input("Whats the name of the second flatmate? ")
f2d = int(input(f"How many days was {f2} in the house during the bill period? "))


#Logic
the_bill = Bill(amount, period)
flatmate1 = Flatmate(name=f1, days_in_house=f1d)
flatmate2 = Flatmate(name=f2, days_in_house=f2d)

print(flatmate1.name, " pays:", flatmate1.pays(bill=the_bill, other_flatmate=flatmate2))
print(flatmate2.name," pays:", flatmate2.pays(bill=the_bill, other_flatmate=flatmate1))

pdf_report = PdfReport(filename=f"Bill from {the_bill.period}.pdf")
pdf_report.generate(flatmate1,flatmate2,the_bill)
