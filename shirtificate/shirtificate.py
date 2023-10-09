from fpdf import FPDF
from PIL import Image

class PDF(FPDF):
    text_hight = 30
    def __init__(self,name):
        self.image("shirtificate.png", w = 210)
        self.set_font("helvetica", "B", 20)
        self.text_color(255,255,255)
        self.text(self.epw/2, self.text_hight*3, f"{name}took CS50")


    def header(self):
        self.set_font("helvetica", "B", 36)
        self.set_x(210 / 2)
        self.cell(
            1,
            self.text_hight,
            "CS50 Shirtificate",
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
        )
        self.ln(10)








def main():
    name = input("Name: ")
    pdf = PDF(name)
    pdf.set_margin(0)
    pdf.add_page()
    pdf.output("test.pdf")

main()