import tempfile

from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas
import qrcode
import qrcode.image.svg
from svglib.svglib import svg2rlg

point = 1
inch = 72


def make_qr_code_drawing(data, size):
    qr = qrcode.QRCode(
        version=2,  # QR code version a.k.a size, None == automatic
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # lots of error correction
        box_size=size,  # size of each 'pixel' of the QR code
        border=4  # minimum size according to spec
        )
    qr.add_data(data)
    qrcode_svg = qr.make_image(image_factory=qrcode.image.svg.SvgPathFillImage)
    svg_file = tempfile.NamedTemporaryFile()
    qrcode_svg.save(svg_file)  # store as an SVG file
    svg_file.flush()
    qrcode_rl = svg2rlg(svg_file.name)  # load SVG file as reportlab graphics
    svg_file.close()
    return qrcode_rl


def make_pdf_file(output_filename, data):
    qrcode_rl = make_qr_code_drawing(data, 20)
    c = canvas.Canvas(output_filename, pagesize=(2 * inch, 0.94 * inch))
    renderPDF.draw(qrcode_rl, c, 0, 0)
    c.setStrokeColorRGB(0,0,0)
    c.setFillColorRGB(0,0,0)
    c.setFont("Helvetica", 12 * point)
    c.drawString( 1.01 * inch, 0.1 * inch, data )
    c.showPage()
    c.save()


if __name__ == "__main__":
    filename = "label.pdf"
    make_pdf_file(filename, "Hello World!")