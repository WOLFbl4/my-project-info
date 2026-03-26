import time
import datetime

class WorkTimeTracker:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start_tracking(self):
        self.start_time = datetime.datetime.now()
        print(f"Tracking started at: {self.start_time}")

    def stop_tracking(self):
        self.end_time = datetime.datetime.now()
        print(f"Tracking stopped at: {self.end_time}")
        self.calculate_time_spent()

    def calculate_time_spent(self):
        if self.start_time and self.end_time:
            time_spent = self.end_time - self.start_time
            print(f"Total time spent: {time_spent}")
        else:
            print("Tracking has not been started or stopped correctly")

if __name__ == '__main__':
    tracker = WorkTimeTracker()
    tracker.start_tracking()
    time.sleep(5)  # Simulate work time
    tracker.stop_tracking()