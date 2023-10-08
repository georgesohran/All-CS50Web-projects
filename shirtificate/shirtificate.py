from fpdf import FPDF
from PIL import Image

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 15)

        # Moving cursor to the right:
        self.cell(30)
        # Printing title:
        self.cell(30, 10, "Title", border=1, align="C")




def main():
    pdf = PDF()
    pdf.add_page()
    shirt = Image.open("shirtificate.png")
    width,hight = shirt.size

    pdf.image("shirtificate.png", 105, 148.5,80)
    pdf.set_title("CS50 Shirtificate")
    pdf.output("test.pdf")

main()