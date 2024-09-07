from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer

class Stopwatch:
    def __init__(self, timer_screen, timer_start, timer_stop, timer_reset):
        self.timer_screen = timer_screen
        self.timer_start = timer_start
        self.timer_stop = timer_stop
        self.timer_reset = timer_reset
        
        self.timer_start.clicked.connect(self.start_timer)
        self.timer_stop.clicked.connect(self.stop_timer)
        self.timer_reset.clicked.connect(self.reset_timer)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.time_remaining = 15 * 60 * 1000  # 15 minutes in milliseconds

    def start_timer(self):
        if not self.timer.isActive():
            self.timer.start(1000)  # Update timer every second

    def stop_timer(self):
        if self.timer.isActive():
            self.timer.stop()

    def reset_timer(self):
        self.stop_timer()
        self.time_remaining = 15 * 60 * 1000
        self.update_display()

    def update_timer(self):
        if self.time_remaining > 0:
            self.time_remaining -= 1000
            self.update_display()
        else:
            self.timer.stop()

    def update_display(self):
        hours, rem = divmod(self.time_remaining // 1000, 3600)
        minutes, seconds = divmod(rem, 60)
        time_str = "{:02}:{:02}".format(minutes, seconds)
        self.timer_screen.setText(time_str)
