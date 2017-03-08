import os
import glob

class cleanup:
    def __init__(self, filepath,extension):
        self.filepath = filepath       
        self.extension = extension 

    def list_files(filepath,extension):
        path = filepath
        extension = extension
        os.chdir(path)
        result = [i for i in glob.glob('*.{}'.format(extension))]
        return(result)     
                 
    def removefiles(filepath,extension):
        
        files = cleanup.list_files(filepath,extension)
        for x in range(len(files)):
            print(files[x])
            if len(files) > 30:
                break
                print('More than 30 files are going to be deleted: breaking operation')
            source_file = filepath+ '\\'+ files[x]
            os.remove(source_file)
                
                 