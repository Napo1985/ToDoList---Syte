# TODO list
This Api supports a basic to do list with the folowing actions:
 * Get all items
 * Add an item
 * Remove an item 
 * Mark as done

A task have the folowing properties: 
 * Task description
 * Time stemp 
 * Is done 
 * Uniq id


#### REST API
#### Get all items
HTTP GET
```
/tasks
Example:
http://localhost:5000/tasks
```

##### Add item
HTTP POST
```
/tasks/user_new_task
Example:
curl -i -H "Content-Type: application/json" -X POST http://localhost:5000/tasks/user_new_task
user_new_task = task description
```

##### Delete item
HTTP DELETE
```
/tasks/id
Example:
curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/tasks/id
id = task id
```

##### Update as done
HTTP PUT
```
/tasks/id
Example:
curl -i -H "Content-Type: application/json" -X PUT http://localhost:5000/tasks/id
id = task id
```


#### Build
Run REST api
``` bash
"full path"\python.exe "full path"\Api.py
```
Run tests
``` bash
"full path"\python.exe "full path"\test_ListActions.py
```



Examples:
```
"C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\python.exe" C:\Rpos\syte\To_Do_List\ToDoList\Api.py

"C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\python.exe" C:\Rpos\syte\To_Do_List\ToDoList\test_ListActions.py
```