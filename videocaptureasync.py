# file: videocaptureasync.py
import threading
import cv2
import copy
class VideoCaptureAsync:
    def __init__(self, width=2688, height=1520):
        self.src = "rtsp://admin:DocoutBolivia@192.168.1.64:554/Streaming/Channels/102/"
        #self.src = "video.mp4"
        
        ##video back_office
        #self.src = "/home/docout/Desktop/Exportación de ACC - 2019-07-10 00.16.18.avi"
        
        ##peaje
        #self.src = '/home/docout/Desktop/Exportación de ACC - 2019-07-09 23.05.46.avi'
        #vide  borading gate
        #self.src = '/home/docout/Desktop/Exportacióself.src = 'rtsp://admin:S1stemas@172.16.20.95/onvif/profile1/media.smp'n de ACC - 2019-07-10 00.43.27.avi'
        #self.src = 'rtsp://admin:S1stemas@172.16.20.116/onvif/profile1/media.smp'
        
        #ip = '172.16.20.98'
        #port =':554'
        #172.16.20.98
        #self.src = 'rtsp://administrator@'+ip#+'/defaultPrimary?streamType=u'#172.16.20.116/onvif/profile1/media.smp'
        #self.src = 'rtsp://administrator@'+ip+port+'/defaultPrimary?streamType=u'
        
        #al frente del back office
        #self.src = 'rtsp://administrator:@172.16.20.98/defaultPrimary?streamType=m'
    
        #self.src = 'rtsp://admin:admin@172.16.20.11/defaultPrimary?streamType=u'
        #self.src = 'rtsp://admin:S1stemas@172.16.20.95/onvif/profile1/media.smp'

        #self.src = 'rtsp://admin:S1stemas@172.16.20.95/onvif/profile1/media.smp'
        self.cap = cv2.VideoCapture(self.src)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.grabbed, self.frame = self.cap.read()
        self.started = False
        self.read_lock = threading.Lock()

    def set(self, var1, var2):
        self.cap.set(var1, var2)

    def start(self):
        if self.started:
            print('[!] Asynchroneous video capturing has already been started.')
            return None
        self.started = True
        self.thread = threading.Thread(target=self.update, args=())
        self.thread.start()
        return self

    def update(self):
        while self.started:
            grabbed, frame = self.cap.read()
            with self.read_lock:
                self.grabbed = grabbed
                self.frame = frame

    def read(self):
        with self.read_lock:
            frame = self.frame.copy()
            grabbed = self.grabbed
        return grabbed, frame

    def stop(self):
        self.started = False
        self.thread.join()

    def __exit__(self, exec_type, exc_value, traceback):
        self.cap.release()