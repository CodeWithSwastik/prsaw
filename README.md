# PRSAW 0.1.0

PRSAW, an acronym for `Python Random Stuff API Wrapper`, is a wrapper for the Random Stuff API.

PyPI: https://pypi.org/project/prsaw/ 

## Installation

You can install released versions of prsaw from the Python Package Index with pip or a similar tool:


**Stable Release:** `pip install prsaw`<br>
**Working Version:** `pip install git+https://github.com/CodeWithSwastik/prsaw.git`


## Example Usage:
```python
>>> from prsaw import RandomStuff

>>> rs = RandomStuff() 
>>> rs.create_session()
>>> rs.get_ai_response("How are you?")
['Fine, and you?']
```



## Functions available:

The current list of functions available are:
    

```python
get_joke(_type = "any")  # Refer to https://api.pgamerx.com/endpoints
get_image(_type = "any") # for all the endpoints
get_ai_response(msg) 
 ```

    
