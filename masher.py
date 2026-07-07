import os
import shutil as sh
import time 

def find_skin_element(element: str, dstn: str, direct: str)->None:
    """
    Method to scrape the skin folder for a specified element.

    element: the name of the element your looking for (include file extension)\n
    dstn: the name of the folder you want to make\n
    direct: the path to your skin folder

    kinda dprecated now just gonna keep it in case tho
    """
    print(direct, 'hai')

    try:
        os.mkdir(path=f'{dstn}')
    except:
        pass
    
    direct.replace('\\','\\')

    for skin in os.listdir(path=direct):

        print(f'currently looking at {skin}')

        for skin_element in os.listdir(path=direct+f'\\{skin}'):
            print(skin_element)
            if skin_element == element:
                print(f'found {skin} {skin_element}')
                try:
                    sh.copy2(src=direct+f'\\{skin}\\{skin_element}',
                            dst=dstn)
                    os.rename(src=f'{dstn}\\{element}',
                            dst=f'{dstn}\\{skin} {element}')
                    
                    print(f'sucessfully copied {skin_element} from {skin}')
                except:
                    continue

