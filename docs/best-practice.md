# Best Practice

This page should give you some common advice on programming exercises.

1. Use [Git](https://docs.github.com/en/get-started/getting-started-with-git) to store your exercises and track changes.
2. Use a proper editor like [PyCharm](https://www.jetbrains.com/pycharm/)
   or [Visual Studio Code](https://code.visualstudio.com/).
3. Only pass primitives, tuples, dictionaries and lists as action parameters.
4. Don't pass secret values (e.g. solutions) as action parameters.
5. Test your exercises well with unit and manual tests.
6. Organize your exercises according to their dependencies.
7. Use the {meth}`entrypoint <pytmlib.entrypoint>` decorator to group and organize exercises.