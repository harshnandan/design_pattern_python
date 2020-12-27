from abc import ABC, abstractmethod

#########################################################
#########################################################

class Spreadsheet(ABC):
    '''
    Abstract document base class
    '''
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def accept(self, visitor_obj):
        raise NotImplementedError


class XLSX_DOC(Spreadsheet):
    '''
    Concrete implementation of document base class
    '''
    def __init__(self, name):
        super().__init__(name+'.xlsx')

    def accept(self, visitor_obj):
        visitor_obj.visitXLSX(self)


class CSV_DOC(Spreadsheet):
    '''
    Concrete implementation of document base class
    '''
    def __init__(self, name):
        super().__init__(name+'.csv')

    def accept(self, visitor_obj):
        visitor_obj.visitCSV(self)


#########################################################
#########################################################
class Visitor(ABC):
    '''
    Visitor Interface
    '''
    @abstractmethod
    def visitXLSX(self, xlsx_obj: XLSX_DOC):
        raise NotImplementedError

    @abstractmethod
    def visitCSV(self, csv_obj: CSV_DOC):
        raise NotImplementedError

class SaveAsXLSX(Visitor):
    '''
    Concrete implementation of visitor interface
    '''
    def visitXLSX(self, xlsx_obj: XLSX_DOC):
        print('Saving {} as {}'.format(xlsx_obj.name, xlsx_obj.name.replace('.xlsx','.xlsx')))

    def visitCSV(self, csv_obj: CSV_DOC):
        print('Saving {} as {}'.format(csv_obj.name, csv_obj.name.replace('.csv','.xlsx')))

class SaveAsPDF(Visitor):
    '''
    Concrete implementation of visitor interface
    '''
    def visitXLSX(self, xlsx_obj: XLSX_DOC):
        print('Saving {} as {}'.format(xlsx_obj.name, xlsx_obj.name.replace('.xlsx','.pdf')))

    def visitCSV(self, csv_obj: CSV_DOC):
        print('Saving {} as {}'.format(csv_obj.name, csv_obj.name.replace('.csv','.pdf')))


class SaveAsPRN(Visitor):
    '''
    Concrete implementation of visitor interface
    '''
    def visitXLSX(self, xlsx_obj: XLSX_DOC):
        print('Saving {} as {}'.format(xlsx_obj.name, xlsx_obj.name.replace('.xlsx','.prn')))

    def visitCSV(self, csv_obj: CSV_DOC):
        print('Saving {} as {}'.format(csv_obj.name, csv_obj.name.replace('.csv','.prn')))

#########################################################
#########################################################

# xlsx file
xl_obj = XLSX_DOC('XL_file')
# csv file
csv_obj = CSV_DOC('CSV_file')

# create objects for all concrete implementations of visitors
v_xlsx = SaveAsXLSX()
v_pdf = SaveAsPDF()
v_prn = SaveAsPRN()

# pass in appropriate visitor in accept method of the obj
xl_obj.accept(v_xlsx)
csv_obj.accept(v_xlsx)

print('')
xl_obj.accept(v_pdf)
csv_obj.accept(v_pdf)

print('')
xl_obj.accept(v_prn)
csv_obj.accept(v_prn)