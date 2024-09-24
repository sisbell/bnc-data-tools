Simple tool for parsing the all the conversations from the British National Corpus Archive into easily readable flat files.

This is useful for visual inspection of spoken conversations for research purposes. 

## Obtaining Spoken Conversation Data
Download the British National Corpus Archive
* Go to http://www.natcorp.ox.ac.uk/
* Click the link for [Download the BNC Baby (4m word sample) from the Oxford Text Archive](https://llds.ling-phil.ox.ac.uk/llds/xmlui/handle/20.500.14106/2553)
* You will see the downloaded 2553.zip archive file. Unarchive it
* Copy the content of the _Texts/K_ directory from the archive to the _data/K_ directory in this Github project

## Running the Scripts
Run the following command from the root of the project
```shell
python -m scripts.convert_conversations
```
## Output
The output of the conversation starts with a simple header that includes the conversation id, the location and the activity.
It then proceeds with each turn for the speaker and their utterance.

```
---| KB0SE000 | 028801 | meeting in street | talking
Margaret: You enjoyed yourself in America
Bob: Eh?
Margaret: did you?
Bob: Oh I covered a nice trip, yes
```
