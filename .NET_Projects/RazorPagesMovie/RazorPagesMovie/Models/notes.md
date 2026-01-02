<!DOCTYPE html>
<html>
<head>
<style>
a { target="_blank"; }
mark 
{
    color: #FFFFFF;
    background-color: #464646ff;
    font-weight: bold;
    padding: 1px 3px;
}
</style>
</head>
<body>

### <a href="https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/model?view=aspnetcore-10.0&tabs=visual-studio-code" target="_blank">Adding models to a Razor Pages app in ASP.NET Core</a>

Classes are added for managing movies in a database. The app's model classes use <a href="https://learn.microsoft.com/en-us/ef/core" target="_blank">Entity Framework Core (EF Core)</a> to work with the database. EF Core is an object-relational mapper (O/RM) that simplifies data access. You write the model classes first, and EF Core creates the database.

The model classes are known as POCO classes (from "**P**lain-**O**ld **C**LR **O**bjects") because they don't have a dependency on EF Core. They define the properties of the data that are stored in the database.

#### The Movie Class

The Movie class contains:

- An ID field to provide a primary key for the database.

- A <a href="https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.dataannotations.datatypeattribute">[DataType]</a> attribute to specify the type of data in the <mark>ReleaseDate</mark> field. With this attribute:
    - The user is not required to enter time information in the date field.
    - Only the date is displayed, not time information.

- The question mark after <mark>string</mark> indicates that the property is nullable. For more information, see <a href="https://learn.microsoft.com/en-us/dotnet/csharp/nullable-references">Nullable reference types.</a>

<a href="https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.dataannotations">DataAnnotations</a> are covered in a later tutorial.

</body>