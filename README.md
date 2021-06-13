# stock-ticker
Files to display stock information on [MAX7219](https://www.maximintegrated.com/en/products/power/display-power-control/MAX7219.html) controlled LED Matrices.

### Preview
- [Video Link](https://www.youtube.com/watch?v=urgL1vKh9yM)

### How-To/Installation:
1. Clone the repo/type `git clone https://github.com/jackokeeffe/stock-ticker.git` into your command prompt.
2. Install BeautifulSoup4 and Pyserial in your Python Enviroment.
3. Install MD_PAROLA in your Arduino IDE.
4. Connect device (see below).
5. Upload `receiveData.ino` to your Arduino.
6. Start `guiAndSerial.py`

### Connecting:
- VCC - 5V
- GND - GND
- CS - 10
- DIN - 11
- CLK - 12

### Built With:
- Python and Arduino.
- Arduino UNO.
- 4 LED Matrices ([Similar Device](https://www.amazon.ca/DAOKI-MAX7219-Control-Display-Raspberry/dp/B07X95H9DT/ref=sr_1_17?dchild=1&keywords=MAX7219%2BMatrix%2BDisplay%2B4%2Bin%2B1&qid=1618942593&sr=8-17&th=1))

### Libraries Used:
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) for collecting stock data from [finance.yahoo.com](finance.yahoo.com).
- [PySerial](https://pythonhosted.org/pyserial/) sending data from Python to Arduino.
- [MD_PAROLA](https://github.com/MajicDesigns/MD_Parola) for displaying stock information on LED Matrices.

### Author:
- Author: Jack O'Keeffe
- [Website](https://jackokeeffe.me)
