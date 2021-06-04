# PRSAW 0.4.0
[![Downloads](https://static.pepy.tech/personalized-badge/prsaw?period=total&units=international_system&left_color=green&right_color=orange&left_text=Downloads)](https://pepy.tech/project/prsaw)

PRSAW, an acronym for `Python Random Stuff API Wrapper`, is a wrapper for the [Random Stuff API](https://api.pgamerx.com/).
PyPI: https://pypi.org/project/prsaw/ 

## Installation

You can install released versions of prsaw from the Python Package Index with pip or a similar tool:

**Stable Release:** `pip install prsaw`<br>
**Working Version:** `pip install git+https://github.com/CodeWithSwastik/prsaw.git`

## Example Usage
```python
# import the module
from prsaw import RandomStuff

# initiate the object
api_key = "Your API Key"
rs = RandomStuff(api_key = api_key) # You can avoid this step if you don't have an api key

# get a response from an endpoint
response =  rs.get_ai_response("How are you?")
print(response)

# close the object once done (recommended)
rs.close()
```

## Example async usage
```python
# import the module
from prsaw import RandomStuff

# initiate the object with async mode
api_key = "Your API Key"
rs = RandomStuff(async_mode = True, api_key = api_key)

# get a joke
joke = await rs.get_joke()
print(joke)

# close the session
await rs.aclose()
```


## Functions available

The current list of asynchronous functions available are:

```python
# endpoints
await get_joke(_type = "any")  # Refer to https://api.pgamerx.com/endpoints
await get_image(_type = "any") # for all the endpoints
await get_ai_response(msg)

# others
await aclose() # closes the object
 ```
 
 ## Important Links
 * Register API key - [Click Here](https://api.pgamerx.com/register)           
 * Documentation/Endpoints - [Click Here](https://api.pgamerx.com/endpoints/)
