import os

print("File iterator remover")
#print(os.walk('C:\Users\BatmanHuntr\Desktop\testdisk-7.2-WIP\recover'))
#for root, dirs, files in os.walk('H:/recover v2'):
#for root, dirs, files in os.walk('C:/Users/BatmanHuntr/Desktop/testdisk-7.2-WIP/recover'):
    #for f in files:
        #if f.endswith("_EXE"):
            #os.remove(os.path.join(root, f))
            #print('deleted:'+root+' '+f)


def filemvr():
    fileExistsErrors = 0
    unknownErrors = 0
    extension = "doc"
    for root, dirs, files in os.walk('F:/Jomar Cloud/Compu Negra Recovery 2023/Unsorted/'):
        for f in files:
            if f.endswith("."+extension):
                print(root+"/"+f)
                try:
                    os.rename((root+"/"+f), ("F:/Jomar Cloud/Compu Negra Recovery 2023/"+extension+"/"+f))
                except FileExistsError:
                    fileExistsErrors += 1 
                    print("already in destination")
                except:
                    unknownErrors += 1
                    print("unknown error")
    print("File Exist Errors: "+str(fileExistsErrors))
    print("Unknown Errors: " + str(unknownErrors))
                
            
filemvr()