#This program utilizes Object-Oriented Programming (OOP) principles and the third-party fpdf2 library to dynamically generate a personalized, single-page PDF document

from fpdf import FPDF
#pdf = FPDF()
#pdf.add_page()
#pdf.output("hello_world.pdf")
#load_image(shirtificate.png)

name=input("Name: ")
pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica', '', 40)
pdf.cell(0, 0, text="CS50 Shirtificate", fill=False, align="C")
pdf.set_font('helvetica', '', 30)
pdf.set_text_color(r=255, g=255, b=255)
pdf.image("shirtificate.png", x="C", y=36)
pdf.cell(h=180 ,text=f"{name} took CS50", fill=False, align="C", center=True)
pdf.output("shirtificate.pdf")