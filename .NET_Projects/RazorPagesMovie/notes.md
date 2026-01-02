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


## Some references used
https://getbootstrap.com/docs/5.3/customize/color-modes/
https://getbootstrap.com/docs/4.0/components/navbar/

---

## Extracted portions from <a href="https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0&tabs=visual-studio-code">ASP.NET Core Tutorial</a>

### Examining the project files
#### Pages folder
A <mark>.cshtml</mark> file that has HTML markup with C# code using Razor syntax.
A <mark>.cshtml.cs</mark> file that has C# code that handles page events.

Supporting files have names that begin with an underscore. For example, the <mark>_Layout.cshtml</mark> file configures UI elements common to all pages. <mark>_Layout.cshtml</mark> sets up the navigation menu at the top of the page and the copyright notice at the bottom of the page. For more information, see Layout in <a href="https://learn.microsoft.com/en-us/aspnet/core/mvc/views/layout?view=aspnetcore-10.0">ASP.NET Core.</a>

#### wwwroot folder
Contains static assets, like HTML files, JavaScript files, and CSS files. For more information, see <a href="https://learn.microsoft.com/en-us/aspnet/core/fundamentals/static-files?view=aspnetcore-10.0">Static files in ASP.NET Core.</a>

##### <mark>appsettings.json</mark>
Contains configuration data, like connection strings. For more information, see <a href="https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-10.0">Configuration in ASP.NET Core.</a>

</body>