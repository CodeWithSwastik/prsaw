# PRSAW 0.2.0

PRSAW, an acronym for `Python Random Stuff API Wrapper`, is a wrapper for the Random Stuff API.
PyPI: https://pypi.org/project/prsaw/ 

## Installation

You can install released versions of prsaw from the Python Package Index with pip or a similar tool:

**Stable Release:** `pip install prsaw`<br>
**Working Version:** `pip install git+https://github.com/CodeWithSwastik/prsaw.git`

## Example Usage:
```python
# import the module
from prsaw import RandomStuff

# initiate the object
rs = RandomStuff()

# get a response from an endpoint
response =  rs.get_ai_response("How are you?")
print(response)

# close the object once done (recommended)
rs.close()
```

## Example async usage:
```python
# import the module
from prsaw import RandomStuff

# initiate the object with async mode
rs = RandomStuff(async_mode=True)

# get a joke
joke = await rs.get_joke()
print(joke)
```

## Functions available:

The current list of asynchronous functions available are:

```python
# endpoints
await get_joke(_type = "any")  # Refer to https://api.pgamerx.com/endpoints
await get_image(_type = "any") # for all the endpoints
await get_ai_response(msg)

# others
await close() # closes the object
 ```
