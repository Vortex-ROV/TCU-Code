from  PyQt5.QtWidgets import QWidget


class Readings:
    def __init__(self, ROVdepth, x_acc, y_acc, z_acc, gyro_x, gyro_y, gyro_z, temp, pressure, lcd ):
        # super(Readings, self).__init__()

        self.ROVdepth = ROVdepth
        self.x_acc = x_acc
        self.y_acc = y_acc
        self.z_acc = z_acc
        self.gyro_x = gyro_x
        self.gyro_y = gyro_y
        self.gyro_z = gyro_z
        self.pressure = pressure
        self.temp = temp
        self.lcd = lcd

    def handle_sensor_logic(self, data):
        data:str = data.decode('utf-8')

        x_acc_read = self.strip(data[0:6])
        y_acc_read = self.strip(data[6:12])
        z_acc_read = self.strip(data[12:18])
        gyro_x_read = self.strip(data[18:24])
        gyro_y_read = self.strip(data[24:30])
        gyro_z_read = self.strip(data[30:36])
        pressure_read = self.strip(data[36:42])
        temp_read = self.strip(data[42:48])

        self.x_acc.setText(f"  X acc: {x_acc_read}")
        self.y_acc.setText(f"  Y acc: {y_acc_read}")
        self.z_acc.setText(f"  Z acc: {z_acc_read}")
        self.gyro_x.setText(f"  Gyro X: {gyro_x_read}")
        self.gyro_y.setText(f"  Gyro Y: {gyro_y_read}")
        self.gyro_z.setText(f"  Gyro Z: {gyro_z_read}")
        self.pressure.setText(f"  Pressure: {pressure_read}")
        self.temp.setText(f"  Temp: {temp_read}")
        self.lcd.display(f"{temp_read}")

    def strip(self, str):
        stripped = str.lstrip('0')
        if stripped == '':
            return "0.0"
        return stripped
