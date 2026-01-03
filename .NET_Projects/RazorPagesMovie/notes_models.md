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

#### Scaffold the movie model

```
dotnet aspnet-codegenerator razorpage -m Movie -dc RazorPagesMovie.Data.RazorPagesMovieContext -udl -outDir Pages/Movies --referenceScriptLibraries --databaseProvider sqlite
```
The following table details the ASP.NET Core code generator options.
| Option                     | Description                                             |
| -------------------------- | ------------------------------------------------------- |
| -m                         | The name of the model.                                  |
| -dc                        | The DbContext class to use including namespace.         |
| -udl                       | Use the default layout.                                 |
| -outDir                    | The relative output folder path to create the views.    |
| --referenceScriptLibraries | Adds _ValidationScriptsPartial to Edit and Create pages |

#### Use SQLite for development, SQL Server for production

When SQLite is selected, the template generated code is ready for development. The following code shows how to select the SQLite connection string in development and SQL Server in production.

##### Program.cs
```
...
builder.Services.AddRazorPages();

if (builder.Environment.IsDevelopment())
{
    builder.Services.AddDbContext<RazorPagesMovieContext>(options =>
        options.UseSqlite(builder.Configuration.GetConnectionString("RazorPagesMovieContext")));
}
else
{
    builder.Services.AddDbContext<RazorPagesMovieContext>(options =>
        options.UseSqlServer(builder.Configuration.GetConnectionString("ProductionMovieContext")));
}
...
```

#### Create the initial database schema using EF's migration feature
Run the following .NET CLI command:
.NET CLI
```
dotnet ef migrations add InitialCreate
```
The <mark>migrations</mark> command generates code to create the initial database schema. The schema is based on the model specified in <mark>DbContext</mark>. The <mark>InitialCreate</mark> argument is used to name the migrations. Any name can be used, but by convention a name is selected that describes the migration.

Run the following .NET CLI command:
.NET CLI
```
dotnet ef database update
```
The <mark>update</mark> command runs the <mark>Up</mark> method in migrations that have not been applied. In this case, <mark>update</mark> runs the <mark>Up</mark> method in the <mark>Migrations/\<time-stamp>_InitialCreate.cs</mark> file, which creates the database.
</body>