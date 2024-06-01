# Backend Development I - MBA Software Engineering -1st SEM - 2024

Sure, here's the translation of the README:

## Using Docker with Python 3.12

- Download this repository

- Open the folder in your preferred editor, such as [Visual Studio Code](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/) 

- Run the command `docker-compose build` to build the Docker image
```
docker-compose build
```

- Now, start the image with `docker-compose up`
``` 
docker-compose up -d
```

- Create your Python files in the `src` folder

## How to run the created files in Docker?

- To run the Python files created in **src**, execute the command:

```
docker-compose exec app python first_class.py
```

> Replace `first_class.py` with the name of the file you want to run.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

by **Eduardo Raider** - Software Engineer