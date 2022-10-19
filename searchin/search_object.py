"""Search a query in an object.
Useful reference: https://docs.python.org/3/library/inspect.html
"""
from collections.abc import Iterable
from inspect import getmembers, isbuiltin, getdoc, getcomments, getfile, getsource, signature
from typing import Union, List, Sized
import numbers


class Node:
    """A node in a path."""

    def __init__(self, name: str, obj, depth: int):
        self.name = name
        self.obj = obj
        self.depth = depth

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.obj == other.obj


class Path:
    """A path."""

    def __init__(self):
        self.last_node = None
        self.names_path = None

    def from_start_node(self, start_node: Node):
        """Create a path from a start node."""
        self.last_node = start_node
        self.names_path = str(start_node)
        return self

    def add_node(self, node: Node):
        """Add a node to the path."""
        new = Path()
        new.last_node = node
        new.names_path = self.names_path + '.' + str(node)
        return new

    def __str__(self):
        return self.names_path


def trunc_str(s: str, max_len: int = 50) -> str:
    """Truncate a string to a maximum length."""
    return s[:max_len] + '...' if len(s) > max_len else s


class SearchMatch:
    """A search match, which is used to represent the position of the found query."""

    def __init__(self):
        self._repr = ''

    def __str__(self):
        return self._repr

    def __repr__(self):
        return self._repr

    def from_number(self, n: str):
        """Represent a match of a number.
        :param n: The number converted to string.
        """
        self._repr = n
        return self

    def from_str(self, s: str, idx: int, search_term: str):
        """Represent a match of a string.
        :param s: The string.
        :param idx: The index of the match.
        :param search_term: The search term.
        """
        # Clean the string: remove newlines and tabs, strip it.
        # Show the beginning of the string, the match, and the end of the string.
        begin = trunc_str(s[:idx].replace('\n', ' ').replace('\t', ' ').strip())
        match = trunc_str(s[idx:idx + len(search_term)].replace('\n', ' ').replace('\t', ' ').strip())
        end = trunc_str(s[idx + len(search_term):].replace('\n', ' ').replace('\t', ' ').strip())
        self._repr = f'{begin}{match}{end}'
        return self

    def from_obj(self, str_obj, idx, search_term):
        """Represent a match of an object."""
        self.from_str(str_obj, idx, search_term)


class SearchResult:
    """A search result, which is returned to the user."""

    def __init__(self, query, path: Path, search_match: SearchMatch):
        self.query = query
        self.path = path
        self.search_match = search_match

    def __str__(self):
        return f""""\"{self.query}\" found in {self.path} : {self.search_match}"""


def is_in(obj, search_term: str) -> Union[bool, SearchMatch]:
    """
    Search an object for a given search term.
    :param obj:
    :param search_term:
    """
    if isinstance(obj, str):
        # Find idx of search term in obj
        idx = obj.find(search_term)
        return SearchMatch().from_str(obj, idx, search_term) if idx != -1 else False
    elif isinstance(obj, numbers.Number):  # Any number (int, float, complex, ...)
        str_obj = str(obj)
        return SearchMatch().from_number(str_obj) if str_obj == search_term else False
    else:
        str_obj = str(obj)
        idx = str_obj.find(search_term)
        return SearchMatch().from_obj(str_obj, idx, search_term) if idx != -1 else False


def is_iterable(obj):
    """Check if an object is iterable."""
    return isinstance(obj, Iterable)


def is_sized_iterable(item: Iterable) -> bool:
    """Check if an iterable is sized."""
    return hasattr(item, '__len__') or isinstance(item, Sized)


def _search_object(obj, query: str, max_depth: int = 10,
                   max_iterable_length: int = 100) -> Union[List[SearchResult], None]:
    """
    Search an object for a given search term.
    :param obj: The object to search in.
    :param query: What to search for.
    :param max_depth: The maximum depth of the recursive search.
    :param max_iterable_length: The maximum length of an iterable to search in.
    :return: A list of search results.
    """
    queue: List[Path] = [Path().from_start_node(Node('root', obj, 0))]
    while queue:
        path = queue.pop(0)
        item = path.last_node.obj
        depth = path.last_node.depth
        if (sr := is_in(item, query)) is not False:
            yield SearchResult(query, path, sr)
        if depth < max_depth:
            if not isbuiltin(item):
                if doc := getdoc(item) is not None:
                    queue.append(path.add_node(Node('', doc, depth + 1)))
                if comments := getcomments(item) is not None:
                    queue.append(path.add_node(Node('', comments, depth + 1)))
                try:
                    file = getfile(item)
                    queue.append(path.add_node(Node('', file, depth + 1)))
                except TypeError:
                    pass
                try:
                    source = getsource(item)
                    queue.append(path.add_node(Node('', source, depth + 1)))
                except (OSError, TypeError):
                    pass
                try:
                    sig = signature(item)
                    queue.append(path.add_node(Node('', sig, depth + 1)))
                except (ValueError, TypeError):
                    pass
                if is_iterable(item):
                    if is_sized_iterable(item) and len(item) < max_iterable_length:
                        queue.extend([path.add_node(Node(str(i), x, depth + 1)) for i, x in enumerate(item)])
                else:
                    queue.extend([path.add_node(Node(name, member, depth + 1))
                                  for name, member in getmembers(item)
                                  if not isbuiltin(member)
                                  ])


def searchin(obj, query: str, max_depth: int = 10, max_iterable_length: int = 100,
                  get_raw_result: bool = False) -> Union[List[SearchResult], None]:
    """
    Search an object for a given search term.
    :param obj: The object to search in.
    :param query: What to search for.
    :param max_depth: The maximum depth of the recursive search.
    :param max_iterable_length: The maximum length of an iterable to search in.
    :param get_raw_result: If True, return the raw results (of type SearchResult), else just print them.
    :return: A list of search results.
    """
    # Assert that `query` is a string
    assert isinstance(query, str), f"Query must be a string, not {type(query)}"

    if get_raw_result:
        return _search_object(obj, query, max_depth, max_iterable_length)
    else:  # Print the results
        for result in _search_object(obj, query, max_depth, max_iterable_length):
            print(result)
