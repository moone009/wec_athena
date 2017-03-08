import bz2
import os
import glob
from wec_athena import cleanup

class athenaprocess:
    def __init__(self, filepath):
        self.filepath = filepath
        self.extension = extension    
        
    def compress(filepath,extension):
        
        compressionLevel = 9
        
        files = cleanup.list_files(filepath,extension)
        print(files)
        for x in range(len(files)):
            print(files[x])
            
            ## Parameters
            source_file = filepath + files[x]
            archive_file = filepath+'Archive\\'+ files[x]
            destination_file = filepath+'CompressedForUpload\\'+files[x]+'.bz2'
            
            ## Compress
            tarbz2contents = bz2.compress(open(source_file, 'rb').read(), compressionLevel)
            fh = open(destination_file, "wb")
            fh.write(tarbz2contents)
            fh.close()
            ## Move File
            os.rename(source_file, archive_file)  
     
     

