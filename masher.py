import os
import shutil as sh
import time

#we'll need a way to scrape everything include the 2x scale elements and save them with the orginally scale element

#ui to display everything wouldn't hurt, maybe flask so i could actual use some mark up and learn npm 

#when the user selects one of the originially scaled elements there will be a function that will search the 2x folder and add it to the new skin

#when a user choose an element it's gonna have to be renamed

#sike were not using a fucking web app frame work nigga were using pyqt



def find_skin_element(element: str, dstn:str):

    try:
        os.mkdir(path=f'{dstn}')
    except:
        pass

    direct: str = input('Please input your skin folder directory')
    direct.replace('\\','\\')

    for skin in os.listdir(path=direct):

        print(f'currently looking at {skin}')

        for skin_element in os.listdir(path=direct+f'\\{skin}'):

            if skin_element == element:
                print(f'found {skin} {skin_element}')
                try:
                    sh.copy2(src=direct+f'\\{skin}\\{skin_element}',
                            dst=dstn)
                    os.rename(src=f'{dstn}\\{element}',
                            dst=f'{dstn}\\{skin} {element}')
                    
                    print(f'sucessfully downloaded {skin_element} from {skin}')
                except:
                    continue


find_skin_element('cursor.png', 'cursors')
