import Tools.PDF as PDF
import PyPDF2 as PyPDF2


class PDF_Modifier:

    def cutPDF(self):
        path = input('Full path of the PDF:')
        pdf1 = PDF.PDF(path)
        if pdf1.check_file:
            page_range = self.get_range_to_cut(pdf1.full_path)
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
        path1 = input('Provide the full path of the first PDF:')
        path2 = input('Provide the full path of the second PDF:')

    def copyPDF(self):
        path = input('Paste the full path of the PDF you would like to copy:')

    def get_range_to_cut(self, path):
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

    def sendEmail(self, attachment):
        print('New PDF sent by email.')
        checker = self.ask("""
Send PDF by email:
    1: YES
    2: NO
        """)
        if checker:
            print('Email sent.')
        else:
            print('Email not sent.')

    def ask(self, message):
        x = False
        answer = False
        while not x:
            rd = input(message)
            if rd == '1':
                answer = True
                x = True
            elif rd == '2':
                answer = False
                x = True
            else:
                print('WARN: Invalid option.')
        return answer
