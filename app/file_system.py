from fnmatch import fnmatch
import os
import os.path
from datetime import datetime, timedelta
from logs import Logs

class FileSystem():

    def __init__(self, archive_path):
        self.archive = archive_path


    def list_files(self, t_path):
        t_files = []
        pattern = "*.jpg"
        for path, subdirs, files in os.walk(t_path):
            for name in files:
                if fnmatch(name, pattern):
                    t_files.append(os.path.join(path, name))
        return t_files
    
    
    def check_files(self, path):
        if not self.list_files(path):
            return False
        return True
    
    def get_creation_date(self, file):
        t = os.path.getmtime(file)
        date = datetime.fromtimestamp(t)
        return date
            
    
    def archive_files(self, files, folder):
        try:
            Logs.Print("Archiving files to " + folder)

            for file in files:
                oldfile = file;
                file_date = str(self.get_creation_date(file))
                newfile = self.archive + "/" + str(file_date).replace(' ', '_').replace('-','_').replace(':','_') + "_" + folder + ".jpg"

                Logs.Print("Archiving file: " + oldfile + " to " + newfile)
                os.rename(oldfile, newfile)

        except Exception as e:
            Logs.Print("Exception: " + str(e))

    def cleanup_archive(self, days):

        files = self.list_files(self.archive)

        for file in files:
            file_date = self.get_creation_date(file)
            date_N_days_ago = datetime.now() - timedelta(days=days)

            if file_date < date_N_days_ago:
                os.unlink(file)




