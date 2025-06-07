import os
from PIL import Image


def thecoppier(dir_path, filetFlag, garsonFlag, patikFlag, bebeFlag, ilkadimFlag):
    
    if filetFlag:
    
        directory = "FİLET"
        parent_dir_fil = dir_path
        dir_path_fil = dir_path
        path = os.path.join(parent_dir_fil, directory)
    
        if "FİLET" not in os.listdir(dir_path_fil):
            os.mkdir(path)
    
        for path in os.listdir(dir_path_fil):
            # if os.path.isfile(os.path.join(dir_path, path)):
            # if (1):
            if (path[-1] == 'g' or path[-1] == 'G'):
    
                thefile = os.path.join(dir_path_fil, path)
                im = Image.open(thefile)
                im.save(f"{parent_dir_fil}\FİLET\{path}")
                
    
                
                
        # namechanger
                
        res = []
        dir_path_fil = f"{parent_dir_fil}\FİLET"
    
        # Iterate directory
        for element in os.listdir(dir_path):
            # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, element)):
                res.append(element)
        # print(res)
    
        newnameler = []
        for i in res:
            oldname = i
            i = list(i)
            if i[-1] == 'G':
                i[2] = 'F'    
                newname = "".join(i)
                
                if newname not in os.listdir(dir_path_fil):
                
                    newname = f"{parent_dir_fil}\FİLET\{newname}"
                    oldname = f"{parent_dir_fil}\FİLET\{oldname}"
                
                    newnameler.append(newname)
                    
                    os.rename(oldname, newname)
                    
                    
                    
                    
                    
    if garsonFlag:
    
        directory = "GARSON"
        parent_dir_gar = dir_path
        dir_path_gar = parent_dir_gar
        path = os.path.join(parent_dir_gar, directory)
    
        if "GARSON" not in os.listdir(dir_path_gar):
            os.mkdir(path)
    
        for path in os.listdir(dir_path_gar):
            # if os.path.isfile(os.path.join(dir_path, path)):
            # if (1):
            if (path[-1] == 'g' or path[-1] == 'G'):
    
                thefile = os.path.join(dir_path_gar, path)
                im = Image.open(thefile)
                im.save(f"{parent_dir_gar}\GARSON\{path}")
                
    
                
                
        # namechanger
                
        res = []
        dir_path_gar = f"{parent_dir_gar}\GARSON"
    
        # Iterate directory
        for element in os.listdir(dir_path_gar):
            # check if current path is a file
            if os.path.isfile(os.path.join(dir_path_gar, element)):
                res.append(element)
        # print(res)
    
        newnameler = []
        for i in res:
            oldname = i
            i = list(i)
            if i[-1] == 'G':
                i[2] = 'G'    
                newname = "".join(i)
                
                if newname not in os.listdir(dir_path_gar):
                
                    newname = f"{parent_dir_gar}\GARSON\{newname}"
                    oldname = f"{parent_dir_gar}\GARSON\{oldname}"
                
                    newnameler.append(newname)
                    
                    os.rename(oldname, newname)
                    
                    
                    
    if patikFlag:
    
        directory = "PATİK"
        parent_dir_pat = dir_path
        dir_path_pat = parent_dir_pat
        path = os.path.join(parent_dir_pat, directory)
    
        if "PATİK" not in os.listdir(dir_path_pat):
            os.mkdir(path)
    
        for path in os.listdir(dir_path_pat):
            # if os.path.isfile(os.path.join(dir_path, path)):
            # if (1):
            if (path[-1] == 'g' or path[-1] == 'G'):
    
                thefile = os.path.join(dir_path_pat, path)
                im = Image.open(thefile)
                im.save(f"{parent_dir_pat}\PATİK\{path}")
                
    
                
                
        # namechanger
                
        res = []
        # burada bir değişikler oldu
        dir_path_pat = f"{parent_dir_pat}\PATİK"
    
        # Iterate directory
        for element in os.listdir(dir_path_pat):
            # check if current path is a file
            if os.path.isfile(os.path.join(dir_path_pat, element)):
                res.append(element)
        # print(res)
    
        newnameler = []
        for i in res:
            oldname = i
            i = list(i)
            if i[-1] == 'G':
                i[2] = 'P'    
                newname = "".join(i)
                
                if newname not in os.listdir(dir_path_pat):
                
                    newname = f"{parent_dir_pat}\PATİK\{newname}"
                    oldname = f"{parent_dir_pat}\PATİK\{oldname}"
                
                    newnameler.append(newname)
                    
                    os.rename(oldname, newname)


    if bebeFlag:
    
        directory = "BEBE"
        parent_dir_beb = dir_path
        dir_path_beb = parent_dir_beb
        path = os.path.join(parent_dir_beb, directory)
    
        if "BEBE" not in os.listdir(dir_path_beb):
            os.mkdir(path)
    
        for path in os.listdir(dir_path_beb):
            # if os.path.isfile(os.path.join(dir_path, path)):
            # if (1):
            if (path[-1] == 'g' or path[-1] == 'G'):
    
                thefile = os.path.join(dir_path_beb, path)
                im = Image.open(thefile)
                im.save(f"{parent_dir_beb}\BEBE\{path}")
                
    
                
                
        # namechanger
                
        res = []
        dir_path_beb = f"{parent_dir_beb}\BEBE"
    
        # Iterate directory
        for element in os.listdir(dir_path_beb):
            # check if current path is a file
            if os.path.isfile(os.path.join(dir_path_beb, element)):
                res.append(element)
        # print(res)
    
        newnameler = []
        for i in res:
            oldname = i
            i = list(i)
            if i[-1] == 'G':
                i[2] = 'B'    
                newname = "".join(i)
                
                if newname not in os.listdir(dir_path_beb):
                
                    newname = f"{parent_dir_beb}\BEBE\{newname}"
                    oldname = f"{parent_dir_beb}\BEBE\{oldname}"
                
                    newnameler.append(newname)
                    os.rename(oldname, newname)

    if ilkadimFlag:

        directory = "İLKADIM"
        parent_dir_ilk = dir_path
        dir_path_ilk = parent_dir_ilk
        path = os.path.join(parent_dir_ilk, directory)

        if "İLKADIM" not in os.listdir(dir_path_ilk):
            os.mkdir(path)

        for path in os.listdir(dir_path_ilk):
            # if os.path.isfile(os.path.join(dir_path, path)):
            # if (1):
            if (path[-1] == 'g' or path[-1] == 'G'):
                thefile = os.path.join(dir_path_ilk, path)
                im = Image.open(thefile)
                im.save(f"{parent_dir_ilk}\İLKADIM\{path}")

        # namechanger

        res = []
        dir_path_ilk = f"{parent_dir_ilk}\İLKADIM"

        # Iterate directory
        for element in os.listdir(dir_path_ilk):
            # check if current path is a file
            if os.path.isfile(os.path.join(dir_path_ilk, element)):
                res.append(element)
        # print(res)

        newnameler = []
        for i in res:
            oldname = i
            i = list(i)
            if i[-1] == 'G':
                i[2] = 'I'
                newname = "".join(i)

                if newname not in os.listdir(dir_path_ilk):
                    newname = f"{parent_dir_ilk}\İLKADIM\{newname}"
                    oldname = f"{parent_dir_ilk}\İLKADIM\{oldname}"

                    newnameler.append(newname)
                    os.rename(oldname, newname)




# thecoppier(r'C:\Users\Aymam\Desktop\dukkan\patikat - cropper deneme\Cropper', 1, 1, 1, 1, 1)
















# dir_path = r'C:\Users\Aymam\Desktop\dukkan\yenice patikle'
# filetFlag = 1

# if filetFlag:

#     directory = "FİLET"
#     parent_dir = dir_path
#     path = os.path.join(parent_dir, directory)

#     if "FİLET" not in os.listdir(dir_path):
#         os.mkdir(path)

#     for path in os.listdir(dir_path):
#         # if os.path.isfile(os.path.join(dir_path, path)):
#         # if (1):
#         if (path[-1] == 'g' or path[-1] == 'G'):

#             thefile = os.path.join(dir_path, path)
#             im = Image.open(thefile)
#             im.save(f"{parent_dir}\FİLET\{path}")
            
# filetFlag = 1
# dir_path = r'C:\Users\Aymam\Desktop\dukkan\yenice patikle'


# if filetFlag:

#     directory = "FİLET"
#     parent_dir = dir_path
#     path = os.path.join(parent_dir, directory)

#     if "FİLET" not in os.listdir(dir_path):
#         os.mkdir(path)

#     for path in os.listdir(dir_path):
#         # if os.path.isfile(os.path.join(dir_path, path)):
#         # if (1):
#         if (path[-1] == 'g' or path[-1] == 'G'):

#             thefile = os.path.join(dir_path, path)
#             im = Image.open(thefile)
#             im.save(f"{parent_dir}\FİLET\{path}")
            

            
            
#     # namechanger
            
#     res = []
#     dir_path = f"{parent_dir}\FİLET"

#     # Iterate directory
#     for element in os.listdir(dir_path):
#         # check if current path is a file
#         if os.path.isfile(os.path.join(dir_path, element)):
#             res.append(element)
#     # print(res)

#     newnameler = []
#     for i in res:
#         oldname = i
#         i = list(i)
#         if i[-1] == 'G':
#             i[2] = 'F'    
#             newname = "".join(i)
            
#             newname = f"{parent_dir}\FİLET\{newname}"
#             oldname = f"{parent_dir}\FİLET\{oldname}"
            
#             newnameler.append(newname)
#             os.rename(oldname, newname)



            
    