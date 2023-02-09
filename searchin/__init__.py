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
from sys import modules
from types import ModuleType
from .search_object import searchin
__all__ = ['searchin']


class CallableModule(ModuleType):
    """Inspired from https://stackoverflow.com/a/74604283"""
    def __init__(self):
        ModuleType.__init__(self, __name__)
        self.__dict__.update(modules[__name__].__dict__)
            
    def __call__(self, *args, **kwargs):
        searchin(*args, **kwargs)
            
    mod_call= __call__
    __all__= list(set(vars().keys()) - {'__qualname__'})

modules[__name__]= CallableModule()
