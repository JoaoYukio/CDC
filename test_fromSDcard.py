import sensor, image, lcd, time
import KPU as kpu
import gc
import os
import utime
import uos


lcd.init()
lcd.clear()

clock = time.clock()

labels_stage1 = ['Rust', 'Brown_Spots', 'Sooty_Molds', 'healthy']
labels_stage2 = ['Cercospora', 'Phoma', 'Leaf_Miner','Red_Spider_Mite']
task_stage1 = kpu.load(0x300000)
task_stage2 = kpu.load(0x500000)

kpu.set_outputs(task_stage1, 0, 1, 1, 4)

kpu.set_outputs(task_stage2, 0, 1, 1, 4)

pred = []
true = []

########### Teste para classe cercospora ######################################
for count in range(26):
    img = image.Image('/sd/imagestest/cercos_resized/cerco ' + '(' +str(count+1) + ')' + '.jpg').to_rgb565(copy=True)
    img.pix_to_ai()

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
    utime.sleep_ms(20)
    pred.append(max_index2)
    true.append(0)
    del img
########### Teste para classe leaf miner ######################################
for count in range(32):
    img = image.Image('/sd/imagestest/miner_resized/miner ' + '(' +str(count+1) + ')' + '.jpg').to_rgb565(copy=True)
    img.pix_to_ai()

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
    utime.sleep_ms(20)
    pred.append(max_index2)
    true.append(2)
    del img

########### Teste para classe phoma ######################################
for count in range(34):
    img = image.Image('/sd/imagestest/phoma_resized/phoma ' + '(' +str(count+1) + ')' + '.jpg').to_rgb565(copy=True)
    img.pix_to_ai()

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
    utime.sleep_ms(20)
    pred.append(max_index2)
    true.append(1)
    del img

########### Teste para classe redspidermite ######################################
for count in range(65):
    img = image.Image('/sd/imagestest/redspider_resized/redspider ' + '(' +str(count+1) + ')' + '.jpg').to_rgb565(copy=True)
    img.pix_to_ai()

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
    utime.sleep_ms(20)
    pred.append(max_index2)
    true.append(3)
    del img

print(pred)
print(true)

with open('/sd/imagestest/pred.txt', "w") as f:
    f.write(str(pred))

with open('/sd/imagestest/true.txt', "w") as f:
    f.write(str(true))

a = kpu.deinit(task_stage1)
a = kpu.deinit(task_stage2)

