### AzoneHelper

Example usage:

```
from azonehelper import AzoneHelper

tipIDs = {
	"WTHR":["473541"]
}

username = "user"
password = "secretpassword"

ah = AzoneHelper(username, password)

ah.perform_transaction("buy", "WTHR", 1, tipIDs) 
```


