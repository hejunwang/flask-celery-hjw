#----------------------------------------------------
#       启动虚拟环境 ,执行监听任务写入1号文件,目前有问题
#----------------------------------------------------
source ../../auto_online_py37_app/bin/activate
celery -A celery_task.tasks worker --loglevel=INFO >1.log