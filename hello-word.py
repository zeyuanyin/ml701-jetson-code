import jetson.inference
import jetson.utils

net = jetson.inference.detectNet('SSD-Mobilenet-v2', threshold=0.5)

print('load model success')

    # while display.IsOpen():
    #     img, width, height = camera.CaptureRGBA()
    #     detections = net.Detect(img, width, height)
    #     display.RenderOnce(img, width, height)
    #     display.SetTitle('Object Detection | Network %.1f FPS'%net.GetNetworkFPS())