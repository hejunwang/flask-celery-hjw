#---------------------------------
# 这是一个测试 ,基本的语法规则 ,如果在执行的时间 出现 /r 报错这些  使用 dos2unix *.sh 执行一次就可以了
#---------------------------------
echo 'test_1'

var1='this is a varchar'
echo ${var1}  ${var1::6}

array_name=(a b c d)
echo 'array 数组'
echo "${array_name[1]}"
echo "${array_name[@]}"

a=5
b=6
result=$[a+b]
echo "result: $result"


#---------函数---------
dofun(){

    echo "this is dofun ()"

}

echo "函数开始执行"
dofun
echo "函数执行结束"
pwd
echo '当前的路径 :'
#pathurl='/root/flask-celery-hjw/flask-celery'
#cd $pathurl

echo "跳转到flask-celery下"
echo "首先删除掉已经存在的日志"
#测试这个文件是否存在
#if [-a result_new.log];
 #   rm result_new.log
  #  echo "delete"
cp result.log result_new.log
echo "copy完成 "