# Groq-VoiceVox

## Links
- [Groq client libraries](https://console.groq.com/docs/libraries)
- [voicevox_engine](https://github.com/VOICEVOX/voicevox_engine/tree/master)
- [voicevox-client](https://github.com/voicevox-client/python)
- [Source of languages.json from ```Mahdipourlotfi``` (modified)](https://gist.github.com/jrnk/8eb57b065ea0b098d571)

## Preparations
1. Install VoiceVox Engine via [official website](https://voicevox.hiroshiba.jp/) or download from [official github releases](https://github.com/VOICEVOX/voicevox_engine/releases) :
![image](https://github.com/LunaticGhoulPiano/Groq-VoiceVox/blob/master/pics/VoiceVox_Engine.jpg?raw=true)
You <b><font color = "red">MUST</font></b> install and run this engine before calling their api, else will get ```httpcore.ConnectError: All connection attempts failed```.
You can test with http://127.0.0.1:50021/docs to check if the system is working.
2. [Applay a Groq api key](https://console.groq.com/keys), create a file ```.env``` and set ```GROQ_API_KEY=<YOUR_GROQ_API_KEY>```.
3. Install required libraries:
```
pip install -r requirements.txt
```

## Example code
You can run an example bot, which will act as an ACGN-like AI Waifu.
```
python example.py
```

## Documentations
### groq_gv.py
To be continued
### voicevox_gv.py
To be continued

## Structure
To be continued