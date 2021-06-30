import dropbox,os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            relative_path = os.path.realpath(local_path,file_from)
            dropbox_path = os.path.join(file_to,relative_path)
        with open(local_path,'rb') as f:
            dbx.files_upload(f.read(),dropbox_path,mode = WriteMode('overwrite'))
def main():
    access_token = 'sl.AztNpg-inn1XSn1sQe3aa-Ecmuxb0nNgJXbwQ4hG0UbuoDxHzJKgs9rWuXfszzJMiK_T1oPNurRNJ_JEPPqtsutXIBxy9H0bDppqP5UAiqO1DXzh3oz6ROegyTNqfrVbTypYVCT4n0tT'
    transferData = TransferData(access_token)
    file_from = input("write the file name which you want to upload")
    file_to = '/class1.py'
    transferData.upload_file(file_from, file_to)
main()