flask
-------------------------------------------------------------------
1.flask-celery 异步任务启动测试
启动监听
celery -A celery_task.tasks worker --loglevel=INFO

2.启动app
python app.py

3. 访问地址
访问http://81.71.102.80:5000/req/add_task
http://81.71.102.80:5000

完成进度 ,目前已经完成了基础框架的搭建 ,测试报告的生成 ,可以进行api接口测试 ,并能输出测试报告,
前端点击操作 , vue ,返回结果 ,celery执行 ,输出测试报告
-------------------------------------------------------------------
pytest
-------------------------------------------------------------------
pytest是一个非常成熟的全功能的Python测试框架，主要特点有以下几点：

1、简单灵活，容易上手，文档丰富；
2、支持参数化，可以细粒度地控制要测试的测试用例；
3、能够支持简单的单元测试和复杂的功能测试，还可以用来做selenium/appnium等自动化测试、接口自动化测试（pytest+requests）;
4、pytest具有很多第三方插件，并且可以自定义扩展，比较好用的如pytest-selenium（集成selenium）、pytest-html（完美html测试报告生成）、pytest-rerunfailures（失败case重复执行）、pytest-xdist（多CPU分发）等；
5、测试用例的skip和xfail处理；
6、可以很好的和CI工具结合，例如jenkins

编写规则
编写pytest测试样例非常简单，只需要按照下面的规则：

测试文件以test_开头（以_test结尾也可以）
测试类以Test开头，并且不能带有 init 方法
测试函数以test_开头
断言使用基本的assert即可

-------------------------------------------------------------------
推送当前的代码到远程的仓库中  参考文档 :https://git-scm.com/book/zh/v2/Git-%E5%9F%BA%E7%A1%80-%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93%E7%9A%84%E4%BD%BF%E7%94%A8
1. 查看当前远程仓库的地址
git remote -v

2. 添加远程仓库的地址
git remote add pb  remote_url
pb 是一个仓库的别名
3. 查询远程具体的仓库     git remote show origin
4.删除 一个远程仓库的地址
git remote remove  origin

5. 推送本地仓库的文件到远程仓库中
git  push pb master
