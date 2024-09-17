from  PyQt5.QtWidgets import QWidget


class Readings:
    def __init__(self, ui):

        self.ui = ui

        self.temp_offset = 0.0
        self.ui.offset_button.clicked.connect(self.set_temp_offset)

    def set_temp_offset(self):
        try:
            self.temp_offset = float(self.ui.offset_input.text())
        except:
            print('Error in offset input')

    def handle_sensor_logic(self, data):
        data:str = data.decode('utf-8')

        # x_acc_read = self.strip(data[0:6])
        # y_acc_read = self.strip(data[6:12])
        # z_acc_read = self.strip(data[12:18])
        # gyro_x_read = self.strip(data[18:24])
        # gyro_y_read = self.strip(data[24:30])
        # gyro_z_read = self.strip(data[30:36])
        pressure_read = self.strip(data[36:42])
        temp_read = self.strip(data[42:48])
        compass_read=self.strip(data[48:51])

        updated_temp = float(temp_read) + self.temp_offset
        

        # self.x_acc.setText(f"  X acc: {x_acc_read}")
        # self.y_acc.setText(f"  Y acc: {y_acc_read}")
        # self.z_acc.setText(f"  Z acc: {z_acc_read}")
        # self.gyro_x.setText(f"  Gyro X: {gyro_x_read}")
        # self.gyro_y.setText(f"  Gyro Y: {gyro_y_read}")
        # self.gyro_z.setText(f"  Gyro Z: {gyro_z_read}")
        # self.ui.pressure.setText(f"  Pressure: {pressure_read}")
        # self.ui.temp.setText(f"  Temp: {str(updated_temp)}")
        # self.ui.compass_label.setText(f"Compass: {str(compass_read)}")
        # self.ui.compass_image.update_angle(int(compass_read))
        # self.ui.lcd.display(f"{str(updated_temp)}")

    def strip(self, str):
        stripped = str.lstrip('0')
        if stripped == '':
            return "0.0"
        return stripped
