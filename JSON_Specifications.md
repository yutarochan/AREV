# JSON Specifications

The following document outlines the specifications used to communicate between the 
client Hololens and the server side compute node.

Under each device are the listed commands which are available for them to issue - 
this will be interpreted by the other device, provided with the return json parameters.

Commands are issued using the `cmd`, along with any other parameters which are specified 
and defined in each of the sections. The return json will include a `resp` code which will
echo back the command issued, following the resulting return values which are defined below.

## Client (Hololens)

### `fetchData`
Send this message after opening a connection with the host node.

The data can be requested in either 3D (by `fetchData3D`) or 2D (by `fetchData2D`)

Arguments:
* `cord`: Sends only the coodinate values without the associated node_id.
* `all`: Sends both the coordinate values with the corresponding node_id.

Parameters: NONE

Input Message:

	{ 
		"cmd": "fetchData3D"， 
		"args": "cord"
	}

Output:
	
	{
		"resp": "get_data3D",
		"data": [[0.23423, 0.23424, 0.9834], ... etc],
		"node_id": ['s8d098f', 's8df900', 'sdf2f32',  ... etc] // Given when passed 'all' parameter.
	}

---
### `getNode`
Gets information about the node. Most likely can be meta data about documents and other key data 
which can be presented in the front end.

Parameters:
* `id`: The node ID to request information on.

Input Message:

	{
		"cmd": "getNode",
		"id": "s8d098f"
	}

Output:

	{
		"resp": "getNode",	
		"node_id": "s8d098f",
		"title": "Bidirectional LSTM-CRF Models for Sequence Tagging",
		"Author": ["Author Test", ... etc],
		"url": "https://arxiv.org/abs/1508.01991"
	}
