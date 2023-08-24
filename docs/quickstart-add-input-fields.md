# Add Input fields

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
