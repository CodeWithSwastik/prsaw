# PRSAW 0.4.0
[![Downloads](https://static.pepy.tech/personalized-badge/prsaw?period=total&units=international_system&left_color=green&right_color=orange&left_text=Downloads)](https://pepy.tech/project/prsaw)

PRSAW, an acronym for `Python Random Stuff API Wrapper`, is a wrapper for the [Random Stuff API](https://api.pgamerx.com/).
PyPI: https://pypi.org/project/prsaw/ 

## Installation

You can install released versions of prsaw from the Python Package Index with pip or a similar tool:

**Stable Release:** `pip install prsaw`<br>
**Working Version:** `pip install git+https://github.com/CodeWithSwastik/prsaw.git`

## Example Usage (No API KEY)
```python
# import the module
from prsaw import RandomStuffV2

# initiate the object
rs = RandomStuffV2() 

# get a response from an endpoint
response = rs.get_ai_response("How are you?")
print(response)

# close the object once done (recommended)
rs.close()
```

## Example async usage (With an API key)
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

## Plans
If you've purchased a premium plan you can pass that as a paramater to RandomStuffV3 or RandomStuffV4
```python
plan = "Can be pro/biz/mega/ultra"
rs = RandomStuffV4(api_key = api_key, plan=plan)
```


## Server (V4)
You can specify the server in RandomStuffV4 if you want
```python
server = "Can be primary/backup/unstable"
rs = RandomStuffV4(api_key = api_key, server=server)
```
## Misc
You can also pass `dev_name`, `bot_name` and `ai_language` as paramaters to RandomStuffV3 or RandomStuffV4.

## Functions available

The current list of asynchronous functions available are:

```python
# endpoints
await get_joke(_type)  # Refer to https://api.pgamerx.com/endpoints
await get_image(_type) # for all the endpoints
await get_ai_response(msg)

# others
await aclose() # closes the object
 ```
 
 ## Important Links
 * Register API key - [Click Here](https://api.pgamerx.com/register)           
 * Documentation/Endpoints - [Click Here](https://api.pgamerx.com/endpoints/)

