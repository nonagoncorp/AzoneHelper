### AzoneHelper

Example usage:

```
tipIDs = {
	"WTHR":["473541"]
}

username = "user"
password = "secretpassword"

ah = AzoneHelper(username, password)

ah.perform_transaction("buy", "WTHR", 1, tipIDs) 
# buy 1 share of WTHR, using hot-tips from the tipIDs dict
```


