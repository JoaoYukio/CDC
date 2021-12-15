import sensor, image, lcd, time
import KPU as kpu
import gc

lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((224, 224))
sensor.set_brightness(2)
sensor.set_auto_gain(1)
sensor.set_vflip(1)
lcd.clear()

clock = time.clock()

labels_stage1 = ['Rust', 'Brown_Spots', 'Sooty_Molds', 'healthy']
labels_stage2 = ['Cercospora', 'Phoma', 'Leaf_Miner','Red_Spider_Mite']
task_stage1 = kpu.load(0x300000)
task_stage2 = kpu.load(0x500000)

kpu.set_outputs(task_stage1, 0, 1, 1, 4)

kpu.set_outputs(task_stage2, 0, 1, 1, 4)

while(True):
    clock.tick()
    #kpu.memtest()
    img = sensor.snapshot()

    #primeiro estágio
    fmap1 = kpu.forward(task_stage1, img)
    plist=fmap1[:]
    pmax=max(plist)
    max_index=plist.index(pmax)
    if labels_stage1[max_index] == 'Brown_Spots':
        #segundo estágio
        fmap2 = kpu.forward(task_stage2, img)
        plist2=fmap2[:]
        pmax2=max(plist2)
        max_index2=plist2.index(pmax2)
        a = img.draw_string(0,0, str(labels_stage2[max_index2].strip()), color=(255,0,0), scale=2)
        a = img.draw_string(0,20, str(pmax2), color=(255,0,0), scale=2)
    else:
        a = img.draw_string(0,0, str(labels_stage1[max_index].strip()), color=(255,0,0), scale=2)
        a = img.draw_string(0,20, str(pmax), color=(255,0,0), scale=2)

    a = lcd.display(img)
    #gc.collect()
    #a = lcd.draw_string(0,50, str(clock.fps()))

a = kpu.deinit(task_stage1)
a = kpu.deinit(task_stage2)

