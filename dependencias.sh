echo "Instalando dependências..."

pyenv shell 3.6.4

python3 -m pip install Pillow
pip install pytesseract
pip install opencv-python
brew install tesseract