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
.alert
{
  background-color: #4a1e04;
  outline-color: #fdcfb4;
  color: var(--theme-text);
  word-wrap: break-word;
  word-break: break-word;
  border: 1px solid #fdcfb4;
  border-radius: .375rem;
  margin-top: 1rem;
  padding: 1rem;
  font-size: 1rem;
  transition: height .5s ease-in,opacity .5s ease-in;
  display: block;
  position: relative;
}
.alert-title
{
    color: #fbcfb4;
    padding-bottom: 5px;
}
</style>
</head>
<body>

### <a href="https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/sql?view=aspnetcore-10.0&tabs=visual-studio-code">Part 4 of tutorial series on Razor Pages</a>

The <mark>RazorPagesMovieContext</mark> object handles the task of connecting to the database and mapping <mark>Movie</mark> objects to database records. The database context is registered with the <a href="https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection?view=aspnetcore-10.0">Dependency Injection</a> container in <mark>Program.cs</mark>

#### <mark>Program.cs</mark>
```
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
```
The ASP.NET Core <a href="https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-10.0">Configuration</a> system reads the <mark>ConnectionString</mark> key. For local development, configuration gets the connection string from the <mark>appsettings.json</mark> file.

#### <mark>appsettings.json</mark>
```
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "AllowedHosts": "*",
  "ConnectionStrings": {
    "RazorPagesMovieContext": "Data Source=RazorPagesMovieContext-ee6737d0-3f26-4ef6-bc1e-c76bcec62def.db"
  }
}
```
<div class="alert"><b><div class="alert-title">NOTE:</div></b>The tutorial used uses a local database that doesn't require the user to be authenticated. Production apps should use the most <a href="https://learn.microsoft.com/en-us/aspnet/core/security/?view=aspnetcore-10.0#secure-authentication-flows">secure authentication flow available.</a></div>
</body>