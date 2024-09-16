class JoystickMapper:

    @staticmethod
    def map(controls: list):
        max_range = 0
        base = 1500
        tolerance = 0.05

        active_channels = []
        active_channels_indices = []
        for i in range(4):
            if controls[i] > tolerance or controls[i] < -tolerance:
                active_channels.append(i)
                active_channels_indices.append(i)

        # throttle (up, down), yaw, forward/backwards, lateral (left, right)
        if controls[10] == 'M' and (len(active_channels) == 1 or 0 not in active_channels_indices):
            # max_range = 350
            max_range = 250
        else:
            # max_range = 200
            max_range = 250
        
        for i in range(len(controls)):
            if i in active_channels:
                if controls[i] > 0:
                    controls[i] = int((controls[i] * max_range) + base)
                elif controls[i] < 0:
                    controls[i] = int((controls[i] * max_range) + base)
            elif i < 4:
                controls[i] = base

        return controls