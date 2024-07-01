# .shp<-->yolo_label
将ArcGis的shp文件的地理坐标与yolo的label.txt相互转换：

## .shp-->yolo_label
首先在ArcGis上对一个.tif的图片进行标注后，
输出带有.shp的文件，这个文件记录了标注的所有框的地理坐标。

运行“shp--xlsx.ipynb”，输入.shp文件的位置，输出所有框的四个点的经纬坐标的xlsx。

运行“xlsx--yolo_label.txt.ipynb”，
输入原tif图像对应的tfw文件中的6个值
 “A像素大小，水平）
  𝐷（像素大小，垂直，通常为负数）
  𝐵（旋转项，行方向）
  𝐶（旋转项，列方向）
  𝐸（左上角X坐标）
  𝐹（左上角Y坐标）”
在
“  image_width = ***
  image_height = *** 
”填上原tif图像的的像素大小。
在pd.read_excel后输入运行“shp--xlsx.ipynb”所得到的.xlsx表格的位置。
最后输出“yolo_label_path.txt”，填上输出txt文件的位置即可。
这样就实现了将.shp文件中的【地理坐标】形式的框转化为【yolo标签】形式的框。
缺点：我这里只有一类标签，涉及多类时，需要进行改动。

运行“yolo_label_verify”可以对生成的yolo_label.txt进行验证。验证准确性。
输入.tif图像的位置，以及运行“xlsx--yolo_label.txt.ipynb”所得到的“yolo_label_path.txt”的位置。
输出'output_kuang.png'带框的png图片，对框的大小及位置进行验证。

## .shp-->yolo_label
运行“yolo.txt--shp.ipynb”，输入.tif\.tfw\.label.txt，在output_shp_path文件夹中输出对应的shp等文件

## .shp将框中图像批量裁剪成一个个小的tif图像，并生成框对应的shp文件保存在文件夹中
运行“shp按框裁剪.ipynb”，输入.shp\.tif，在output_folder文件夹中输出多个子文件夹，
每个子文件夹中保存小的tif以及对应的shp文件。便于在ArcGis中打开

基于chatgpt-4o
