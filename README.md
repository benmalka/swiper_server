## Server's API

* [Details](#details)
* [Pages](#pages)
  * [Add user](#add-user)
  * [Get items](#get-items)
  * [Like item](#like-item)
  * [Get liked items](#get-liked-items)
  * [Delete item from liked items](#delete-liked-item)

## Details

* Server name: swiper-server.herokuapp.com:80
* Host: heroku

## Pages

### `add user`
Insert user to DB, if exist update user

  * URL: clientapi_v1/add_user
  * Method: POST
  * Type: JSON
  * Data: {“userName”: type.str, “userID” : type.str, “userEmail”: type.str}
  * Returns: {“output”: “success/failed”}


### `get items`
Get items from DB

  * URL: clientapi_v1/get_items
  * Method: POST
  * Type: JSON
  * Data: {“userID”: type.str, “maxPrice”: type.int, “page” : type.int}
  * Returns: Array of item by page (10 per page)

### `like item`
Insert item ID to users “like items” DB (it will be saved only from 24 hours)

  * URL: clientapi_v1/like_item
  * Method: POST
  * Type: JSON
  * Data: {“userID”: type.str, “itemID” :type.str}
  * Returns: {“output”: “success/failed”}

### `get liked items`
Get liked itemed from user “liked items” DB

  * URL: clientapi_v1/get_liked_items
  * Method: POST
  * Type: JSON
  * Data: {“userID”: type.str, “page”: type.int}
  * Returns: Array of items by page (30 per page)

### `delete liked item `
Remove item ID from user’s “like items” DB

  * URL: clientapi_v1/delete_liked_item
  * Method: POST
  * Type: JSON
  * Data: {“userID”: type.str, “itemID”: type.str}
  * Returns: {“output”: “success/failed”}
