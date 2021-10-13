from PyQt5.QtCore import QObject, pyqtSignal
import serial, serial.tools.list_ports
from PyQt5.QtWidgets import QMessageBox

class customSerial(QObject): 
//change file
    dataA = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.serialPort = serial.Serial()
        self.serialPort.timeout = 0.5
        self.serialPort.baudrate =115200


    def update_ports(self):
        self.portList = [port.device for port in serial.tools.list_ports.comports()]


    def connect_serial(self):
        try:
            self.serialPort.open()

        except:

            self.show_popup()



    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("update Window")
        msg.setText("Please UPDATE WINDOW and RECONNCT USB")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)

        x = msg.exec_()

    def read_serial(self):
        while (self.serialPort.is_open):
            data = self.serialPort.readline().decode("utf8").strip()
            if(len(data)>1):
                self.dataA.emit(data)
            print(data)