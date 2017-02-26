using UnityEngine;
using System.Collections;
using System.IO;

public class JsonRead : MonoBehaviour {

    string pathCmd;
    string jsonCmd;

	void Start()
	{
       // readOnly
       
        //obtain the path
        pathCmd = Application.streamingAssetsPath + "/cmd.json";
        jsonCmd = File.ReadAllText(pathCmd);

        //pass data
        Command fetchData = JsonUtility.FromJson<Command>(jsonCmd);
        Debug.Log(fetchData.cmd);
        Debug.Log(fetchData.args);

        string newCmd = JsonUtility.ToJson(fetchData);
        Debug.Log(newCmd);

    }
}


[System.Serializable]
public class Command
{
    public string cmd;
    public string args;
}
