# TrollBot

A small Python script to generate strange strings of text

## Usage

TrollBot has been tested on Python 3.9.5

### Import trollbot into your script:

```python
import trollbot_core as trollbot


#TrollBot functions

trollbot.DebugEnable()

trollbot.GenerateName()

trollbot.GenerateMessage()
```

## Explanation for each function:

#

## `DebugEnable()`

Enables debugging. Will print most of the important things the script is doing to the console. 

#### Example:

```
>>> import trollbot_core as trollbot

>>> trollbot.DebugEnable()

[DEBUG] Debugging started
[DEBUG] Importing 'datetime'
[DEBUG 2022-03-27 23:05:38.039542] Imported 'datetime'

>>> trollbot.GenerateName()

[DEBUG 2022-03-27 23:05:51.483178] Generating a name with type 'random'
[DEBUG 2022-03-27 23:05:51.483201] nametype='random', choosing random name type
[DEBUG 2022-03-27 23:05:51.483216] Generating a type 'weird2' name...
[DEBUG 2022-03-27 23:05:51.483226] Finished generating name
'slagon'
```

#

## `GenerateName(nametype)`

Generates a random internet username.

### Types of names:
> Note: "nametype" will default to "random" when not specified

### dsmp:
Makes a Dream SMP related name.

```python
GenerateName('dsmp')
```

### weird:
Generates a weird name consisting of 2 words.

```python
GenerateName('weird')
```

### weird2:
Attempts to create a "modern" and/or "cool" name.

```python
GenerateName('weird2')
```

### sus:
Generates an Among Us related name.

```python
GenerateName('sus')
```

### hypixel:
Generates a name you might see on the popular Minecraft network Hypixel.

```python
GenerateName('hypixel')
```

### random:
Chooses a random name type from the list above

```python
GenerateName()
GenerateName('random')
```

### `GenerateName()` Example:

```py
>>> from trollbot_core import GenerateName

>>> GenerateName('dsmp') 
'WilburIscool'

>>> GenerateName('weird')
'bedabuser'

>>> GenerateName('weird2')
'BOGUH'

>>> GenerateName('sus')
'gusisbad'

>>> GenerateName('hypixel')
'OhInsane'
```

#

## `GenerateMessage(messagetype)`

Attempts to create a strange message that may or may not make sense.

### Types of messages:
> Note: "messagetype" will default to "random" when not specified

### cringe:
Calls something cringe.

```python
GenerateMessage('cringe')
```

### sus:
Calls something suspicious.

```python
GenerateMessage('sus')
```

### twitter:
Generates a message like those found on Twitter. (cope harder)

```python
GenerateMessage('twitter')
```

### funny:
Says "LOL" or "LUL" in different variations.

```python
GenerateMessage('funny')
```

### good:
Calls something "good"

```python
GenerateMessage('good')
```

### dsmp:
Generates a Dream SMP related message.

```python
GenerateMessage('dsmp')
```

### poop:
Will say that it is constipated or similar.

```python
GenerateMessage('poop')
```

### game:
Will say that it likes a certain game.

```python
GenerateMessage('game')
```

### random:
Chooses a random message type from the list above

```python
GenerateMessage()
GenerateMessage('random')
```

### `GenerateMessage()` Example:

```py
>>> from trollbot_core import GenerateMessage

>>> GenerateMessage('cringe')
"brother that's cringe"

>>> GenerateMessage('sus')
'that is amogus man '

>>> GenerateMessage('twitter')
'take a dump + L + L + cope harder'

>>> GenerateMessage('funny')
'LOL'

>>> GenerateMessage('good')
"man that's poggers"

>>> GenerateMessage('dsmp')
'I LOVE wilbur :two_hearts:'

>>> GenerateMessage('poop')
'help im really constipated rn :weary:'

>>> GenerateMessage('good')
"that's awesome bro"

>>> GenerateMessage()
"that's insane broski"
```