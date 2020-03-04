import Tools.PDF as PDF
import PyPDF2 as PyPDF2

def get_all_range_of_pdf(path):
    lecture = open(path, 'rb')
    read = PyPDF2.PdfFileReader(lecture)
    limitMax = read.getNumPages()
    return [1, limitMax]

def get_range_to_cut(path):
    checker = False
    while not checker:
        limitMin = input("Page to start the PDF:")
        limitMax = input("Page to finish the PDF:")
        lecture = open(path, 'rb')
        read = PyPDF2.PdfFileReader(lecture)
        try:
            if read.getNumPages() >= int(limitMax) and int(limitMin) >= 1 and int(limitMax) >= int(limitMin):
                checker = True
            else:
                print('NOTE: Values not admited.')
        except:
            print('The values provided are not numbers.')
    return [limitMin, limitMax]


def ask(message):
    x = False
    answer = False
    while not x:
        rd = input(message)
        if rd == '1' or rd.lower() == 'yes':
            answer = True
            x = True
        elif rd == '2' or rd.lower() == 'no':
            answer = False
            x = True
        else:
            print('WARN: Invalid option.')
    return answer


class PDF_Modifier:

    def cutPDF(self):
        pdf1 = PDF.PDF(input('Full path of the PDF:'))
        if pdf1.check_file:
            page_range = get_range_to_cut(pdf1.full_path)
            pdfFileObj = open(pdf1.full_path, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            pdfWriter = PyPDF2.PdfFileWriter()
            x = (int(page_range[0]) - 1)
            while x <= (int(page_range[1]) - 1):
                pdfWriter.addPage(pdfReader.getPage(int(x)))
                x += 1
            full_path_new_file = pdf1.path + "\\" + input('Provide a name for the file:') + ".pdf"
            with open(full_path_new_file, 'wb') as outfile:
                pdfWriter.write(outfile)
            self.sendEmail(full_path_new_file)
            print('PDF saved locally as: ' + full_path_new_file)
        elif not pdf1.check_file:
            print('The file is not a PDF.')

    def joinPDF(self):
        pdf1 = PDF.PDF(input('Provide the full path of the first PDF:'))
        pdf2 = PDF.PDF(input('Provide the full path of the second PDF:'))
        if pdf1.check_file and pdf2.check_file:
            page_range1 = get_all_range_of_pdf(pdf1.full_path)
            page_range2 = get_all_range_of_pdf(pdf2.full_path)
            pdfFileObj1 = open(pdf1.full_path, 'rb')
            pdfFileObj2 = open(pdf2.full_path, 'rb')
            pdfReader1 = PyPDF2.PdfFileReader(pdfFileObj1)
            pdfReader2 = PyPDF2.PdfFileReader(pdfFileObj2)
            pdfWriter = PyPDF2.PdfFileWriter()
            x = (int(page_range1[0]) - 1)
            while x <= (int(page_range1[1]) - 1):
                pdfWriter.addPage(pdfReader1.getPage(int(x)))
                x += 1
            x = (int(page_range2[0]) - 1)
            while x <= (int(page_range2[1]) - 1):
                pdfWriter.addPage(pdfReader2.getPage(int(x)))
                x += 1
            full_path_new_file = pdf1.path + "\\" + input('Provide a name for the file:') + ".pdf"
            with open(full_path_new_file, 'wb') as outfile:
                pdfWriter.write(outfile)
            self.sendEmail(full_path_new_file)
            print('PDF saved locally as: ' + full_path_new_file)
        else:
            print('WARN: One or both files are not PDF.')

    def join_range_of_PDFs(self):
        pdf1 = PDF.PDF(input('Provide the full path of the first PDF:'))
        pdf2 = PDF.PDF(input('Provide the full path of the second PDF:'))
        if pdf1.check_file and pdf2.check_file:
            page_range1 = get_range_to_cut(pdf1.full_path)
            page_range2 = get_range_to_cut(pdf2.full_path)
            pdfFileObj1 = open(pdf1.full_path, 'rb')
            pdfFileObj2 = open(pdf2.full_path, 'rb')
            pdfReader1 = PyPDF2.PdfFileReader(pdfFileObj1)
            pdfReader2 = PyPDF2.PdfFileReader(pdfFileObj2)
            pdfWriter = PyPDF2.PdfFileWriter()
            x = (int(page_range1[0]) - 1)
            while x <= (int(page_range1[1]) - 1):
                pdfWriter.addPage(pdfReader1.getPage(int(x)))
                x += 1
            x = (int(page_range2[0]) - 1)
            while x <= (int(page_range2[1]) - 1):
                pdfWriter.addPage(pdfReader2.getPage(int(x)))
                x += 1
            full_path_new_file = pdf1.path + "\\" + input('Provide a name for the file:') + ".pdf"
            with open(full_path_new_file, 'wb') as outfile:
                pdfWriter.write(outfile)
            self.sendEmail(full_path_new_file)
            print('PDF saved locally as: ' + full_path_new_file)
        else:
            print('WARN: One or both files are not PDF.')

    def copyPDF(self):
        pdf1 = PDF.PDF(input('Paste the full path of the PDF you would like to copy:'))
        if pdf1.check_file :
            pdfFileObj1 = open(pdf1.full_path, 'rb')
            pdfReader1 = PyPDF2.PdfFileReader(pdfFileObj1)
            pdfWriter = PyPDF2.PdfFileWriter()
            pdfWriter.cloneReaderDocumentRoot(pdfReader1)
            full_path_new_file = pdf1.path + "\\" + input('Provide a name for the file:') + ".pdf"
            with open(full_path_new_file, 'wb') as outfile:
                pdfWriter.write(outfile)
            self.sendEmail(full_path_new_file)
            print('PDF saved locally as: ' + full_path_new_file)
        else:
            print('WARN: One or both files are not PDF.')

    def sendEmail(self, attachment):
        print('New PDF sent by email.')
        checker = ask("""
Send PDF by email:
    1: YES
    2: NO
        """)
        if checker:
            print('Email sent.')
        else:
            """Email not sent"""

