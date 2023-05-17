git add -A && \
git commit -m "made changes to the images" && \
git push origin macaz


docker build -t devopmacaz/sosotech-website:1.0.0 .
docker run -itd -p  5000:5000 devopmacaz/sosotech-website:1.0.0



***Install SQLAlchemy Flask-SQLAlchemy on windows***

```
py -m pip install SQLAlchemy Flask-SQLAlchemy
```

from flask_sqlalchemy import SQLAlchemy  --> in app.py, uncomment line 5
