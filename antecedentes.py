from fpdf import FPDF

espacio = ((' '))*25

pdf = FPDF('P', 'mm', 'letter')

pdf.add_page()
pdf.set_font("times", "B", 12)
pdf.image('ESCUDO.png', x=56, y=10, w = 15, h = 0, type = 'PNG')
pdf.ln(15)
pdf.cell(105, 5, 'REPÚBLICA DE CUBA', 0, 1, 'C')
pdf.cell(105, 5, 'MINISTERIO DE JUSTICIA', 0, 1, 'C')
pdf.cell(105, 5, 'Registro Central de Sancionados', 0, 0, 'C')
pdf.cell(0, 5, 'SELLO', 0, 1, 'C')
pdf.cell(105, 5, 'CERTIFICACIÓN DE ANTECEDENTES PENALES', 0, 1, 'C')
pdf.ln(10)
pdf.cell(55, 6, 'Nombre:', 'LTR', 0, 'L')
pdf.cell(65, 6, 'Primer apellido:', 'LTR', 0, 'L')
pdf.cell(0, 6, 'Segundo apellido:', 'LTR', 1, 'L')
pdf.cell(55, 6, '', 'LBR', 0, 'L')
pdf.cell(65, 6, '', 'LBR', 0, 'L')
pdf.cell(0, 6, '', 'LBR', 1, 'L')

pdf.cell(40, 6, 'Fecha de nacimiento:', 'LTR', 0, 'L')
pdf.cell(80, 6, 'Padre:', 'LTR', 0, 'L')
pdf.cell(0, 6, 'Madre:', 'LTR', 1, 'L')
pdf.cell(40, 6, '', 'LBR', 0, 'L')
pdf.cell(80, 6, '', 'LBR', 0, 'L')
pdf.cell(0, 6, '', 'LBR', 1, 'L')

pdf.cell(65, 6, 'Lugar de nacimiento:', 'LTR', 0, 'L')
pdf.cell(35, 6, 'Ciudadanía:', 'LTR', 0, 'L')
pdf.cell(35, 6, 'Identidad:', 'LTR', 0, 'L')
pdf.cell(20, 6, 'Sexo:', 'LTR', 0, 'L')
pdf.cell(0, 6, 'Piel:', 'LTR', 1, 'L')

pdf.cell(65, 6, '', 'LBR', 0, 'L')
pdf.cell(35, 6, '', 'LBR', 0, 'L')
pdf.cell(35, 6, '', 'LBR', 0, 'L')
pdf.cell(20, 6, '', 'LBR', 0, 'L')
pdf.cell(0, 6, '', 'LBR', 1, 'L')

pdf.set_font("times", "", 12)

pdf.cell(0 , 5, "El Director del Registro Central de Sancionados, confrontados los archivos de antecedentes penales bajo su ",'LTR',1,'C')
pdf.cell(0 , 5, "     custodia con las generales de la persona que arriba se consigna CERTIFICA QUE:", 'LR',1,'L')

for i in espacio:
    pdf.cell(0, 6, i[0], 'LR', 1, 'C')

pdf.set_font("times", "B", 12)
pdf.cell(100, 6, 'Válida su presentación durante 6 meses después de', 'L', 0, 'C')
pdf.cell(45, 6, '', 0, 0, 'C')
pdf.cell(0, 6, 'Director', 'R', 1, 'L')

pdf.cell(0, 2, ' ', 'LBR', 1, 'C')

pdf.set_title(title='CERTIFICACIÓN DE ANTECEDENTES PENALES.')
pdf.set_author(author='Lázaro Hernández Galbán')
pdf.set_creator(creator='Organización Nacional de Bufetes Colectivos')
pdf.output("ANTECEDENTES.pdf")