# Code for Camera control


import picamera   # picamera 라이브러리 임포트
import time       # time 라이브러리 임포트

with picamera.PiCamera() as camera:

    camera.resolution = (1024, 768)


    # 프리뷰 화면 표시
    camera.start_preview()

    # 촬영하고 파일 저장
    camera.start_recording(output = filename + '.h264')

    # 5초 대기
#    camera.wait_recording(5)

    # Button down stop
    if


    # 프리뷰 화면 종료
    camera.stop_preview()

    # 촬영 종료
    camera.stop_recording()
