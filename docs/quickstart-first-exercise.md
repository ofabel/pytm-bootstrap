# First Exercise

After successful [installation of this library](/installation) you can start creating your first exercise. Open your
Python project folder (where your virtual environment folder is located) in your
favourite IDE and create a new file named `app.py` with the following content:

```{literalinclude} ./code/first-exercise.py
```

The `version` property defines the current version of your exercise. Use semantic versioning according to
the [specification](https://semver.org/spec/v2.0.0.html).

The `start` method with the `entrypoint` decorator defines the entrypoint of your exercise. This method will be
executed, when your exercise starts.

Now, open a new console window, navigate to the python project folder, activate the virtual environment and execute the
following command:

```shell
flask run
```

Open the _Python Tool Manager_ and create a new exercise. Start the preview mode, and you should see the following:

![first exercise in preview mode](./graphs/first-exercise.png)

In order to upload your exercise, you need to create a [Dockerfile](https://docs.docker.com/engine/reference/builder/)
at the same level as your `app.py` file is located and add the following content:

```dockerfile
FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir gunicorn
    
CMD gunicorn -b 0.0.0.0:8080 app:app
```

Now you can upload your first exercise.