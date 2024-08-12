# .shp<-->yolo_label
将ArcGis的shp文件的地理坐标与yolo的label.txt相互转换：

## 切割+替换/早期
运行“切割+替换.ipynb”，将一张大图切割成具体的尺寸的小图，并把改后缀为jpg便于yolo处理。

## .shp-->yolo_label
首先在ArcGis上对一个.tif的图片进行标注后，
输出带有.shp的文件，这个文件记录了标注的所有框的地理坐标。

运行“shp--xlsx.ipynb”，输入.shp文件的位置，输出所有框的四个点的经纬坐标的xlsx。

运行“xlsx--yolo_label.txt.ipynb”，
输入原tif图像对应的tfw文件中的6个值<br/>
 “A像素大小，水平）<br/>
  𝐷（像素大小，垂直，通常为负数）<br/>
  𝐵（旋转项，行方向）<br/>
  𝐶（旋转项，列方向）<br/>
  𝐸（左上角X坐标）<br/>
  𝐹（左上角Y坐标）”<br/>
在
“  image_width = ***
  image_height = *** 
”填上原tif图像的的像素大小。<br/>
在pd.read_excel后输入运行“shp--xlsx.ipynb”所得到的.xlsx表格的位置。<br/>
最后输出“yolo_label_path.txt”，填上输出txt文件的位置即可。<br/>
这样就实现了将.shp文件中的【地理坐标】形式的框转化为【yolo标签】形式的框。<br/>
缺点：我这里只有一类标签，涉及多类时，需要进行改动。<br/>

运行“yolo_label_verify”可以对生成的yolo_label.txt进行验证。验证准确性。<br/>
输入.tif图像的位置，以及运行“xlsx--yolo_label.txt.ipynb”所得到的“yolo_label_path.txt”的位置。<br/>
输出'output_kuang.png'带框的png图片，对框的大小及位置进行验证。<br/>

## yolo_label-->.shp
运行“yolo.txt--shp.ipynb”，输入.tif\.tfw\.label.txt，在output_shp_path文件夹中输出对应的shp等文件

## .shp将框中图像批量裁剪
裁剪成一个个小的tif图像，并生成框对应的shp文件保存在文件夹中<br/>
运行“shp按框裁剪.ipynb”，输入.shp\.tif，在output_folder文件夹中输出多个子文件夹<br/>
每个子文件夹中保存小的tif以及对应的shp文件。便于在ArcGis中打开<br/>
------------------------应需求对批量裁剪进行更新[2024年7月4日]-------------------------<br/>
缺点：发现上面的批量裁剪代码裁剪时，其中tif图像的倾角发生变换<br/>
并且部分图形从矩形变成了平行四边形，但不是裁剪的shp文件的问题<br/>
因为我运行拼接shp的代码输出的merge.shp与ArcGIS标注输出的output.shp文件打开是完全一致的<br/>
优化：新的plus代码在裁剪时使用的外接矩形来进行裁剪，不存在变换角度与形状的问题，但标注的图像范围稍大了一点。<br/>
## .shp按框的外接矩形批量裁剪plus\2024年7月4日
运行“shp按框的外接矩形裁剪plus”.ipynb,输入input_tif 的位置、input_shp 的位置，在output_dir文件夹中输出按外接矩形裁的图片。

## 图像批量提取并reset像素大小\2024年7月6日
经过上面的“shp按框的外接矩形批量裁剪plus”之后，会得到一个文件夹里包含了很多子文件夹<br/>
子文件夹里是每个按框裁剪的小图以及所对应的shp文件<br/>
运行“图像批量提取+reset”.ipynb，首先将所有子文件夹中的图片提取到一个新文件夹中<br/>
再将所有像素大小不一的tif图的尺寸全部转为400*400以供后续使用。<br/>

## 多个.shp文件拼接为一个整体的shp文件\2024年7月3日
运行“多shp拼接为整体.ipynb”<br/>
输入“shp按框裁剪.ipynb”运行得到的output_folder文件夹（包括多个子文件夹，内含有裁剪出的小图tif与对应的shp文件）<br/>
确定地理坐标系，这里使用WGS84（即EPSG:4326）<br/>
确定输出．shp（整体的shp文件）的位置。<br/>

## yolo模型推理得到标注的txt文件\2024年7月3日
运行“txt生成.py”，导入预训练好的模型，导入测试的图片，生成经yolo推理得到的框对应的txt文件。<br/>

基于chatgpt-4o<br/>
