# Django-dashboard

A bioinformatic dashboard build by Django web framework. 
=======
## Django代码结构

```bash
< PROJECT ROOT >
   |
   |-- core/                            
   |    |-- settings.py                  # Project Configuration  
   |    |-- urls.py                      # Project Routing
   |
   |-- home/
   |    |-- views.py                     # APP Views 
   |    |-- urls.py                      # APP Routing
   |    |-- models.py                    # APP Models 
   |    |-- tests.py                     # Tests  
   |    |-- templates/                   # Theme Customisation 
   |         |-- includes                # 
   |              |-- custom-footer.py   # Custom Footer      
   |     
   |-- requirements.txt                  # Project Dependencies
   |
   |-- env.sample                        # ENV Configuration (default values)
   |-- manage.py                         # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />



## 部署

克隆项目：

```
git clone https://github.com/czhcooper/Django-dashboard.git
cd Django-dashboard
```

安装依赖：

```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

设置数据库：

```
python manage.py makemigrations
python manage.py migrate
```

在`core/setting.py` 中添加：

```
ALLOWED_HOSTS = ['example.com','www.example.com'] #你的域名
CSRF_TRUSTED_ORIGINS = ['https://example.com', 'https://www.example.com']
```

运行项目：

```
python manage.py runserver 
```

