一、环境准备
1. python 3.9.13
2. django 4.2.7
3. node.js 20.10.0
4. vue 2.5.2

二、后端准备
1. 修改setting.py，配置mysql，新手建议在自己本地搞一个mysql服务


DATABASES = {

    'default': {
    
        'ENGINE': 'django.db.backends.mysql',
        
        'NAME': 'test01', // 你自己的数据库的名字
        
        'USER': 'root',
        
        'PASSWORD': '123',
        
        'HOST': '127.0.0.1',
        
        'PORT': '3306'
        
    }
       
}



3. 数据迁移
切到项目根目录下执行

python manage.py makemigrations

python manage.py migrate

这样我在项目代码里面创建的表就会更新到你本地的数据库里面

4. 启动项目
python manage.py runserver 9999

5. 其他
启动过程中可能需要安装一些python的三方库类，按照报错提示安装就行了，前后端代码全部都是OK的，前提是你环境都OK的情况下


![image](https://github.com/panhui123123/myweb/assets/77530466/708f6079-7105-4922-9745-5cba4f66010e)
