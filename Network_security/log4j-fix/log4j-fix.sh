#!/bin/sh

function log4Update(){
	#echo "所有需要替换的jar包如下："
	#echo "**************************"
	find / -path "/proc" -prune -o -type f -name "log4j-*-2*.jar" -print
	#echo "**************************"
	#echo "搜索完毕，准备替换。。。"
	for file in `find / -path "/proc" -prune -o -type f -name "log4j-*-2*.jar" -print`
	do
  	  for i in  $(dirname "$file")
    	do
    		for j in $file
					do
				  	#获取旧包的用户组属性
					  	user=`ls -l $j |awk -F " " '{print $3}'`
						group=`ls -l $j |awk -F " " '{print $4}'`

						#获取jar包的完整名称
						name3=`echo $j | awk -F "/" '{print$NF}'`

						#获取jar包的完整版本号
						name4=`echo $name3 | awk -F "-" '{print$NF}'`

						#获取jar包的大版本号，1-2-3中的1
						dbb=`echo $name4 | awk -F "." '{print$1}'`

						#获取jar包的中版本号，1-2-3中的2
						zbb=`echo $name4 | awk -F "." '{print$2}'`

						#获取jar的名称(不带版本号)
						name2=`echo $name3 | awk -F "-2" '{print$1}'`
						if [[ "$dbb" = 2  ]];then
							for s in $(ls $(cd "$(dirname "$0")"; pwd)/log4j2-17)
								do
									name4_s=`echo $s | awk -F "-" '{print$NF}'`
									dbb_s=`echo $name4_s | awk -F "." '{print$1}'`
									zbb_s=`echo $name4_s | awk -F "." '{print$2}'`
									name3_s=`echo $s | awk -F "-2" '{print$1}'`
									if [ "$name2" = "$name3_s" ] && [ "$dbb" = "$dbb_s" ] && [ "$zbb" -lt "$zbb_s" ];then
										echo "正在替换中。。。"
										echo "cp $(cd "$(dirname "$0")"; pwd)/log4j2-17/$name3_s-$name4_s $i/" >> replace.log
										mkdir -p $i/bak
										mv  $i/$name2-$name4 $i/bak/$name2-$name4.bak
										cp $(cd "$(dirname "$0")"; pwd)/log4j2-17/$name3_s-$name4_s $i/
										chown $user:$group $i/$name3_s-$name4_s
										chmod 644 $i/$name3_s-$name4_s
									fi
								 done
						fi
        	done
    	done
	done
	
	echo "+++++替换完成！+++++"

}

function log4Check(){
	temp="0"
	for file in `find / -path "/proc" -prune -o -type f -name "log4j-*-2*.jar" -print`
	
	do
  	  for i in  $(dirname "$file")
    		do
    		for j in $file
					do
				  	#获取旧包的用户组属性
					  	user=`ls -l $j |awk -F " " '{print $3}'`
						group=`ls -l $j |awk -F " " '{print $4}'`

						#获取jar包的完整名称
						name3=`echo $j | awk -F "/" '{print$NF}'`

						#获取jar包的完整版本号
						name4=`echo $name3 | awk -F "-" '{print$NF}'`

						#获取jar包的大版本号，1-2-3中的1
						dbb=`echo $name4 | awk -F "." '{print$1}'`

						#获取jar包的中版本号，1-2-3中的2
						zbb=`echo $name4 | awk -F "." '{print$2}'`

						if [[ "$dbb" = 2  &&  "$zbb" -lt 16 ]];then
							echo "发现相关包存在风险:"
							echo $i/$name3
							temp="1"
      			fi
      			
      			if [[ "$dbb" = 2  &&  "$zbb" = 16 ]];then
							temp="2"
      			fi
					done
    		done
	done
	
	if [[ "$temp" = 1 ]];then
			echo "检测到有漏洞风险的Log4j版本,建议升级!"
	else
			echo "未检测到有漏洞风险的Log4j版本，无需升级！"
	fi
}


command=$1
case $command in
  (check)
     log4Check
     ;;
  (update)
     log4Update
     ;;
     (*)
     echo "Error command"
     ;;
esac

