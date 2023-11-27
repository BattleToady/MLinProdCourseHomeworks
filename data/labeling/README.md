How to deploy label-studio:

1. Install label-studio by pip or choose another way(https://labelstud.io/guide/install):

```pip install label-studio```

2. Start label-studio server:

```label-studio start```

3. Create project, Import data and add our labeling interface code:

```
<View>
    <Header value="Table with {key: value} pairs"/>
    <Table name="table" value="$json"/>
    <Choices name="choice" toName="table">
        
        
    <Choice value="Budget form"/><Choice value="Contract form"/></Choices>
</View>``` 
