import dropbox
import os
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    def uploadfiles(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)
def main():
    access_token = 'gcO18ccN1AwAAAAAAAAAAQm584HR4Ot7AjvJBc97KdJdigMcI3UPsY8BKz2QEVv5'
    transferdata = TransferData(access_token)
    file_from = input("Enter the file to transfer:")
    file_to = input("Enter the full path of the file to transfer to dropbox:")
    transferdata.uploadfiles(file_from,file_to)
    print("Transfering is done!")
main()
       
