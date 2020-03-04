
class PDF:

    def __init__(self, path):
        self.full_path = path
        temp = path.split('\\')
        self.name = temp[-1]
        self.path = '\\'.join(temp[:-1])
        self.check_file = PDF.validate_PDF(self.full_path)

    @staticmethod
    def validate_PDF(pdf1_full_path):
        if pdf1_full_path.endswith('.pdf'):
            return True
        else:
            return False



