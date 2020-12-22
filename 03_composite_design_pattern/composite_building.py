from abc import ABC, abstractmethod

class Component(ABC):
    '''
    Component Interface class
    '''
    def __init__(self, name):
        self.name = name
        
    
    @abstractmethod
    def get_size(self):
        pass


class File(Component):
    '''
    File is leaf node
    '''
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size
    
    def get_size(self):
        return self.size


class Folder(Component):
    '''
    Folder is composite 
    '''
    def __init__(self, name):
        super().__init__(name)
        self.child_dict = dict()

    def add(self, comp: Component):
        self.child_dict[comp.name] = comp
    
    def remove(self, comp: Component):
        del self.child_dict[comp.name]

    def get_size(self, value=None):
        total_size = 0
        for name, comp in self.child_dict.items():
            total_size += comp.get_size()
        return total_size

    def get_folder_content(self, indent=''):
        contentStr = '\n{}{:20s}{}'.format(indent, self.name, self.get_size())

        for name, comp in self.child_dict.items():
            if isinstance(comp, Folder):
                contentStr += comp.get_folder_content(indent + '    ')
            else:
                contentStr += '\n{}{:20s}{}' .format(indent + '    ', comp.name, comp.size)
        return contentStr

file_1 = File('file_a.txt', 10)
file_2 = File('file_b.txt', 42)
file_3 = File('file_c.txt', 30)
file_4 = File('file_d.txt', 90)

folder_1 = Folder('folder_1')
folder_1.add(file_1)
folder_1.add(file_2)
folder_2 = Folder('folder_2')
folder_2.add(folder_1)
folder_2.add(file_3)
folder_2.add(file_4)

print('\n*********************************')
print('{:20s}{}'.format('File/Folder', 'Size'))
print('*********************************')
print(folder_2.get_folder_content())
