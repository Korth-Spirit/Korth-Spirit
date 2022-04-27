# The Spirit of Korth

The Spirit of Korth is a python wrapper for the Active Worlds Software Development Kit (SDK). Active Worlds is a trade mark of Active Worlds Inc. The SDK is a set of tools for developing games, bot, and extensions for the Active Worlds platform. The SDK and its license are available at [http://www.activeworlds.com/sdk/download.htm](http://www.activeworlds.com/sdk/download.htm). This project is not affiliated with Active Worlds Inc.

The Spirit of Korth is licensed under the MIT license. All other code is owned by the author. The Spirit of Korth is not affiliated with Active Worlds Inc.

# Installation

This package is provided as a python package. To install it, run the following command:

```python
pip install korth-spirit
```

You will also need to inlcude the SDK with name 'aw64.dll' in the same directory as executing script. There were unexpected issues when calling `aw_create` when accepting an dynamic path to the library.

# Usage

Please know this package is in alpha and a work in progress. The API is subject to change. The spirit of korth is not yet ready for use. You may attempt to use it, but you should not expect it to work.


[Greeter Bot example](https://github.com/Korth-Spirit/Greeter-Bot/blob/9b5c3332206d1ba78bca4bafb7ea6915d0492a97/greeter/__main__.py) using the Korth Spirit wrapper for the Active Worlds SDK.
```python
from korth_spirit import ConfigurableInstance, EventEnum
from korth_spirit.configuration import (AggregateConfiguration,
                                        InputConfiguration, JsonConfiguration)

with ConfigurableInstance(
    AggregateConfiguration(
        configurations={
            JsonConfiguration: ('configuration.json',),
            InputConfiguration: (),
        }
    )
) as bot:
    bot.bus.subscribe(
        EventEnum.AW_EVENT_AVATAR_ADD,
        lambda e: bot.say(f"Salutations {e.avatar_name}!")
    )
        
    bot.main_loop()
```

# License

This project, the Spirit of Korth, is licensed under the MIT license. All other code is owned by the author. The Spirit of Korth is not affiliated with Active Worlds Inc. This project is not affiliated with Active Worlds Inc. The license for Active Worlds Software Development Kit (SDK) is available at [http://www.activeworlds.com/sdk/download.htm](http://www.activeworlds.com/sdk/download.htm).

# Contribution

This project is open source. Feel free to contribute to the project by making a pull request, creating an issue ticket, or sending an email to [Johnny Irvin](mailto:irvinjohnathan@gmail.com). This project, the Spirit of Korth is not affiliated with Active Worlds Inc. Johnathan Irvin is not affiliated with Active Worlds Inc.
