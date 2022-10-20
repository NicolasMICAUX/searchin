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
Cherchez ce que vous voulez dans un objet, méthode ou variable python, directement dans votre code !
    <br />
<!--
    <a href="https://github.com/NicolasMICAUX/searchin"><strong>Explorer la documentation »</strong></a>
-->
    <br />
    <br />
    <a href="https://github.com/NicolasMICAUX/searchin">Voir la démo</a>
    ·
    <a href="https://github.com/NicolasMICAUX/searchin/issues">Report Bug</a>
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## Introduction

<!-- [Screen Shot][product-screenshot] -->

Avez vous déjà passé des heures à chercher le nom d'une méthode ou d'une propriété d'une librairie tierce ? Vous êtes sûr que cette méthode/propriété doit exister, mais impossible de la trouver, ni dans la documentation, ni dans les exemples, ni sur StackOverflow... Vous finissez par vous résigner à scroller dans le code source de la librairie... Tellement frustrant !

Search'In est un outil qui vous permet de rechercher dans des objets python comme si vous étiez sur Google, juste en ajoutant une ligne en plein milieu de votre code !

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>

<!-- GETTING STARTED -->
## Pour commencer
Utiliser Search'In ne recquiert aucun effort.

Installer Search'In avec pip :
```sh
pip install searchin
```

Importer Search'In dans votre code, en ajoutant cette ligne :
```python
from searchin import searchin
```

Pour chercher `"name"` dans une classe `Human` par exemple, il suffit d'ajouter cette ligne :
```python
searchin(Human, "name")
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## D'autres exemples
Vous pouvez chercher n'importe quelle chaîne de caractère dans n'importe quel "entité" python : variable, méthode, objet, classe, module, etc.

**Chercher `"5"` dans un `tuple`**
```python
searchin((1, 2, 3, 4, 5, 6, 7, 8, 9), "5")
# >>> "5" found in root.4 : 5
```

**Chercher `"mean"` dans la méthode `torch.nn.functional.cross_entropy`**
```python
searchin(torch.nn.functional.cross_entropy, "mean")
# >>> "mean" found in root. : def cross_entropy( [...] reduction: str = "mean", [...], label_smoothing)
```

**Chercher `"grad"` dans un `torch.nn.Module`**
```python
model = torch.nn.Linear(10, 10)
searchin(model, "grad")
# >>> "grad" found in root.bias
# >>> "grad" found in root.requires_grad_
# >>> "grad" found in root.weight
# >>> "grad" found in root.zero_grad
```

## Fonctionnalités avancées
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
| [Fuzzy match](https://github.com/NicolasMICAUX/searchin/discussions/2)              | 5/5        | 2/5        | NOBODY            | _e.g._ : `batch_size` should match when searching `batchsize`.                                                                                 |
| [Underline the match](https://github.com/NicolasMICAUX/searchin/discussions/4)      | 4/5        | 1/5        | NOBODY            | _e.g._ : the printed result should be formatted like this : _def cross_entropy( [...] reduction: str = "<u>mean</u>", [...], label_smoothing)_ |
| [Write some tests](https://github.com/NicolasMICAUX/searchin/discussions/5)         | 4/5        | 2/5        | NOBODY            | Write some tests to ensure that the code is working properly.                                                                                  |
| [Find a better algorithm](https://github.com/NicolasMICAUX/searchin/discussions/7)  | 3/5        | 4/5        | NOBODY            | The current algorithm is a BFS (Breadth First Search). Maybe there is a better algorithm to use.                                               |
| [`Searchin...` animation](https://github.com/NicolasMICAUX/searchin/discussions/9)  | 3/5        | 1/5        | NOBODY            | Add a cool animation when searching takes a bit of time.                                                                                       |
| [Profile code](https://github.com/NicolasMICAUX/searchin/discussions/11)             | 2/5        | 1/5        | NOBODY            | Profile the code to see if we can speed it up a little.                                                                                        |
| [Add a CLI](https://github.com/NicolasMICAUX/searchin/discussions/12)                | 1/5        | 2/5        | NOBODY            | Think about the design of a CLI (Command Line Interface) to use Search'In from the terminal.                                                   |

Non-Code contribution :

| Task                     | Importance | Difficulty | Contributor on it | Description                                                                                                                                                           |
|:-------------------------|------------|------------|-------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Adding documentation](https://github.com/NicolasMICAUX/searchin/discussions/6)     | 4/5        | 1/5        | NOBODY            | Add some helpful docstrings, write basic tutorials with real-life scenarios, write a wiki for other contributors to better understand the functioning of the library. |


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


## Auteurs
Cette librairie a été crée par [Nicolas MICAUX](https://github.com/NicolasMICAUX).



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

