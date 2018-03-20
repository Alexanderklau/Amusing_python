check_file所含文件

checkDiskBadSectors.sh 作用：解压checkDiskBadSectors.tar.gz到/opt文件夹下，添加crontable定时任务，六点启动
create_file.py 作用：生成1000个大小为100M的测试文件，位于/infinity/下，大小，个数可以自己去修改.
checkDiskBadSectors.tar.gz 作用：解压后生成一个checkDiskBadSectors.py文件，去读取/infinity/下所用文件，并且将读取错误的文件写入日志。

