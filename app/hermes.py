import os
import sys
import datetime
import time
import yaml
from send_email import SendEmail
from file_system import FileSystem
from google_drive import MyGoogleDrive
from logs import Logs

class Hermes():

    def __init__(self, conf_file):
        self.pidfile = "/tmp/hermes.pid"
        self.conf_file = conf_file
        self.__lock_pid()
        self.conf_data = self.__read_conf()

        # Initiate objects
        self.file_system = FileSystem(self.conf_data['archive_path'])
        self.mail = SendEmail(self.conf_data['mail'])


    def __exit__(self):
        os.unlink(self.pidfile)

    def __read_conf(self):
        with open(self.conf_file) as f:
            yaml_data = yaml.load(f)

        return yaml_data

    def __lock_pid(self):
        self.pid = str(os.getpid())
        if os.path.isfile(self.pidfile):
            Logs.Print("%s already exists, exiting" % self.pidfile)
            sys.exit()
        
        with open(self.pidfile, 'w') as fwrie:
             fwrie.write(self.pid)

    def app(self):

        Logs.Print("Starting Hermes App..")

        while 1:
            try:
                for monitor_path in self.conf_data['monitor_paths']:

                    # Check if there are any files in these paths
                    files = self.file_system.list_files(monitor_path['path'])

                    # wait 2 seconds for ftp transfer
                    time.sleep(2)

                    if files:
                        time_now = datetime.datetime.utcnow()
                        print("\n\n")
                        Logs.Print("======================================================")
                        Logs.Print(str(time_now) + ":    Found alarm on "  + monitor_path['name'])

                        # Create google_drive object 
                        google_drive = MyGoogleDrive(self.conf_data['gdrive_cred_path'])

                        # Upload images into google drive
                        for file in files:
                            google_drive.push(file, monitor_path['gdrive_folder_id'])

                        self.mail.sendMessage(file, monitor_path['name'])
                        self.file_system.archive_files(files, monitor_path['name'])

            except Exception as e:
                Logs.Print("Exception: " + str(e))

    def cleanup(self):

        Logs.Print("Starting Hermes Cleanup..")

        gdrive_folder_ids = []
        retention = self.conf_data['retention']
        for folder_id in self.conf_data['monitor_paths']:
            gdrive_folder_ids.append(folder_id)

        while 1:
            try:
                Logs.Print("Start cleaning process.")

                self.file_system.cleanup_archive(retention)
                google_drive = MyGoogleDrive(self.conf_data['gdrive_cred_path'])
                google_drive.cleanup(retention, gdrive_folder_ids)

                Logs.Print("Stop cleaning process.")

                time.sleep(86400)
            except Exception as e:
                Logs.Print("Exception: " + str(e))

if __name__ == "__main__":

    conf_file = sys.argv[1]
    hermes = Hermes(conf_file)

    if len(sys.argv) > 2 and sys.argv[2] == "cleanup":
        hermes.cleanup()
    else:
        hermes.app()