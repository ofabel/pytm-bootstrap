# Quickstart

This page should give you guidance to create your first exercises.

## First Exercise

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

## Input fields

In order to create a dynamic exercise, we need to allow the user to enter data and send it to the exercise Python code.
So replace the `app.py` file of your first exercise from the example above with the following code:

```{literalinclude} ./code/add-input-fields.py
```

The number field has the name `answer`. The same identifier occurs as parameter in the `solve` method. Field name and
method parameter name have to match in order to use the field's value inside an action. An action is equal to a method
invocation and is represented by a blue button in the user interface:

![add input fields exercise in preview mode](./graphs/add-input-fields-exercise.png)

To control what method is executed after a click on the button, you need to pass a method reference in the invocation of
`add_action`. You can also pass additional values using keyword parameters. See the next chapter for more information on
passing parameters.

## Dynamic Values

An exercise with fixed values is not very interesting and fun to solve. Therefore, we need to introduce dynamic values:

```{literalinclude} ./code/dynamic-values.py
```

As we can see in this slightly advanced version of the second example exercise, the `solve` method has now three
additional parameters namely `m`,`b` and `y`. The values of these parameters are generated in the `start` method and
passed as keyword arguments in the invocation of `add_action`.
