from PIL import Image
import pytesseract as pyt
import cv2
import os

class Convert:
    def menu():
        print("******************")
        print("Formato do arquivo")
        print("******************")
        op = input()
        return op


    def conversor():
        op = Convert.menu()        
        arquivo = input('Nome do arquivo: ')
        imagem = cv2.imread(arquivo+"."+op)
        
        filenameImagem = "{}.png".format(os.getpid())
        cv2.imwrite(filenameImagem, imagem)
        
        texto = pyt.image_to_string(Image.open(filenameImagem))

        os.remove(filenameImagem)
        
        print(texto)

        imagem = cv2.resize(imagem,None,fx=0.25, fy=0.25, interpolation = cv2.INTER_CUBIC)

        #cv2.imshow("imagem contendo o texto", imagem)
        cv2.waitKey(0)
        cv2.destroyAllWindows()