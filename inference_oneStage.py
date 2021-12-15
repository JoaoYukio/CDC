import sensor, image, lcd, time
import KPU as kpu
lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((224, 224))
sensor.set_brightness(2) # Ajuste de -2 a 2, somente int
sensor.set_auto_gain(1)
sensor.set_vflip(1)
lcd.clear()

labels = ['Healthy','Phoma', 'Sooty Molds', 'Red S. Mite','Rust','Cercospora','L. Miner']

'''
0_Cercospora
0_Rust
1_Phoma
2_Leaf_Miner
2_Sooty_Molds
3_Red_Spider_Mite
Healthy
'''

clock = time.clock()

task = kpu.load(0x300000) #change to "/sd/name_of_the_model_file.kmodel" if loading from SD card
kpu.set_outputs(task, 0, 1, 1, 7) #the actual shape needs to match the last layer shape of your model

while(True):
    clock.tick()
    #kpu.memtest()
    img = sensor.snapshot()
    #img = img.rotation_corr(z_rotation=90.0)   uncomment if need rotation correction - only present in full maixpy firmware
    #a = img.pix_to_ai()
    fmap = kpu.forward(task, img)
    plist=fmap[:]
    pmax=max(plist)
    max_index=plist.index(pmax)
    a = img.draw_string(0,0, str(labels[max_index].strip()), color=(255,0,0), scale=2)
    a = img.draw_string(0,20, str(pmax), color=(255,0,0), scale=2)
    #print((pmax, labels[max_index].strip()))
    a = lcd.display(img)
    print(clock.fps())

a = kpu.deinit(task)
