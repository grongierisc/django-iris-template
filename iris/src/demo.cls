Class iris.demo Extends %Persistent
{

/// Description
Property Name As %String;

/// Description
Property Age As %Integer;

Property Stream As %Stream.GlobalBinary;

Storage Default
{
<Data name="demoDefaultData">
<Value name="1">
<Value>%%CLASSNAME</Value>
</Value>
<Value name="2">
<Value>Name</Value>
</Value>
<Value name="3">
<Value>Age</Value>
</Value>
<Value name="4">
<Value>Stream</Value>
</Value>
</Data>
<DataLocation>^iris.demoD</DataLocation>
<DefaultData>demoDefaultData</DefaultData>
<IdLocation>^iris.demoD</IdLocation>
<IndexLocation>^iris.demoI</IndexLocation>
<StreamLocation>^iris.demoS</StreamLocation>
<Type>%Storage.Persistent</Type>
}

}
