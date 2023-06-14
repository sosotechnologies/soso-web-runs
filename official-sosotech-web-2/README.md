git add -A && \
git commit -m "made changes to the images" && \
git push origin macaz


docker build -t sosotech/sosotech:1.0.0 .
docker run -itd -p  5000:5000 sosotech/sosotech:1.0.0



***Install SQLAlchemy Flask-SQLAlchemy on windows***

```
py -m pip install SQLAlchemy Flask-SQLAlchemy
```

from flask_sqlalchemy import SQLAlchemy  --> in app.py, uncomment line 5

***look at the versions of your python Flask dependencies using command***
Example:

```
pip3 show flask
pip3 show Flask-WTF
```

***NOTE:***
in app.py, Database is defined in lines 21 -->
