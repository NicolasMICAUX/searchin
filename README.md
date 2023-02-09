<a name="readme-top"></a>
[![Contributors][contributors-shield]][contributors-url]<!--[![Forks][forks-shield]][forks-url]-->
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]<!--[![MIT License][license-shield]][license-url]--><!--[![LinkedIn][linkedin-shield]][linkedin-url]-->
[![PyPi version][pypi-shield]][pypi-url]
[![Python 2][python2-shield]][python-url]
[![Python 3][python3-shield]][python-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">

  <a href="https://github.com/NicolasMICAUX/searchin">
    <img src="https://raw.githubusercontent.com/NicolasMICAUX/searchin/main/images/logo.png" alt="Logo" width="160" height="160">
  </a>

  <h3 align="center">Search'In</h3>

  <p align="center">
    Search anything in a live python object, method or variable!
    <br />
<!--
    <a href="https://github.com/NicolasMICAUX/searchin"><strong>Explore the docs »</strong></a>
-->
    <br />
    <br />
    <a href="https://github.com/NicolasMICAUX/searchin">View Demo</a>
    ·
    <a href="https://github.com/NicolasMICAUX/searchin/issues">Report Bug</a>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [Screen Shot][product-screenshot] -->

Have you ever spent hours looking for the name of a method or property of a third party library? You are sure that this method/property must exist, but you cannot find it, neither in the documentation, nor in the examples, nor on StackOverflow... You end up scrolling through the source code of the library... So frustrating!

Search'In is a tool that allows you to search in python objects as if you were on Google, just by adding a line in the middle of your code !

<!-- GETTING STARTED -->
## Getting Started
Using Search'In requires no effort at all!

Install Search'In with pip :
```sh
pip install searchin
```

Import Search'In in your code, by adding this line :
```python
import searchin
```

To search for `"name"` in a `Human` class for example, just add this line :
```python
searchin(Human, "name")
```

<!-- USAGE EXAMPLES -->
## Other examples
You can search for any string in any python "entity" : variable, method, object, class, module, etc.

**Search for `"5"` in a `tuple`**
```python
searchin((1, 2, 3, 4, 5, 6, 7, 8, 9), "5")
# >>> "5" found in root.4 : 5
```

**Search for `"mean"` in the method `torch.nn.functional.cross_entropy`**
```python
searchin(torch.nn.functional.cross_entropy, "mean")
# >>> "mean" found in root. : def cross_entropy( [...] reduction: str = "mean", [...], label_smoothing)
```

**Search for `"grad"` in a `torch.nn.Module`**
```python
model = torch.nn.Linear(10, 10)
searchin(model, "grad")
# >>> "grad" found in root.bias
# >>> "grad" found in root.requires_grad_
# >>> "grad" found in root.weight
# >>> "grad" found in root.zero_grad
```

## Advanced features
```python
def searchin(obj,
             query: str,
             max_depth: int = 3,
             top_k_results: int = 10,
             max_iterable_length: int = 100,
             get_raw_result: bool = False) -> Union[List[SearchResult], None]:
    """
    Search an object for a given search term.
    :param obj: The object to search in.
    :param query: What to search for.
    :param max_depth: The maximum depth of the recursive search.
    :param top_k_results: The maximum number of results to return.
    :param max_iterable_length: The maximum length of an iterable to search in.
    :param get_raw_result: If True, return the raw results (of type SearchResult), else just print them.
    :return: A list of search results.
    """
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing
_(Section in english)_  
I want to add a lot of functionnalities to this project, but I don't have much time to work on it. Contributions are welcome!  

<!-- ROADMAP-->
### Roadmap/todo
<!-- table with columns : task, importance, difficulty, status, description -->
| Task                     | Importance | Difficulty | Contributor on it | Description                                                                                                                                    |
|:-------------------------|------------|------------|-------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|
| Fuzzy match              | 5/5        | 2/5        | NOBODY            | _e.g._ : `batch_size` should match when searching `batchsize`.                                                                                 |
| Underline the match      | 4/5        | 1/5        | NOBODY            | _e.g._ : the printed result should be formatted like this : _def cross_entropy( [...] reduction: str = "<u>mean</u>", [...], label_smoothing)_ |
| Write some tests         | 4/5        | 2/5        | NOBODY            | Write some tests to ensure that the code is working properly.                                                                                  |
| Find a better algorithm  | 3/5        | 4/5        | NOBODY            | The current algorithm is a BFS (Breadth First Search). Maybe there is a better algorithm to use.                                               |
| `Searchin...` animation  | 3/5        | 1/5        | NOBODY            | Add a cool animation when searching takes a bit of time.                                                                                       |
| Profile code             | 2/5        | 1/5        | NOBODY            | Profile the code to see if we can speed it up a little.                                                                                        |
| Add a CLI                | 1/5        | 2/5        | NOBODY            | Think about the design of a CLI (Command Line Interface) to use Search'In from the terminal.                                                   |

Non-Code contribution :

| Task                     | Importance | Difficulty | Contributor on it | Description                                                                                                                                                           |
|:-------------------------|------------|------------|-------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Adding documentation     | 4/5        | 1/5        | NOBODY            | Add some helpful docstrings, write basic tutorials with real-life scenarios, write a wiki for other contributors to better understand the functioning of the library. |


_For every todo, just click on the link to find the discussion where I describe how I would do it._  
See the [open issues](https://github.com/NicolasMICAUX/searchin/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### How to contribute
Contributing is an awesome way to learn, inspire, and help others. Any contributions you make are **greatly appreciated**, even if it's just about styling and best practices.

If you have a suggestion that would make this project better, please fork the repo and create a pull request.  
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourAmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Authors
This library was created by [Nicolas MICAUX](https://github.com/NicolasMICAUX).


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/NicolasMICAUX/searchin.svg?style=for-the-badge
[contributors-url]: https://github.com/NicolasMICAUX/searchin/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/NicolasMICAUX/searchin.svg?style=for-the-badge
[stars-url]: https://github.com/NicolasMICAUX/searchin/stargazers
[issues-shield]: https://img.shields.io/github/issues/NicolasMICAUX/searchin.svg?style=for-the-badge
[issues-url]: https://github.com/NicolasMICAUX/searchin/issues
[pypi-shield]: https://img.shields.io/pypi/v/searchin.svg?style=for-the-badge
[pypi-url]: https://pypi.org/project/searchin/
[python2-shield]: https://img.shields.io/badge/python-2.7+-blue.svg?style=for-the-badge
[python3-shield]: https://img.shields.io/badge/python-3.5+-blue.svg?style=for-the-badge
[python-url]: https://www.python.org/downloads/

[//]: # ([license-shield]: https://img.shields.io/github/license/NicolasMICAUX/searchin.svg?style=for-the-badge)
[//]: # ([license-url]: https://github.com/NicolasMICAUX/searchin/blob/master/LICENSE.txt)
[//]: # ([linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555)
[//]: # ([linkedin-url]: https://linkedin.com/in/othneildrew)
[product-screenshot]: images/screenshot.png

