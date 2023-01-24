using System;

static class LogLine
{
    public static string Message(string logLine){
        string[] words = logLine.Split(' ');
        foreach (var word in words) {
            System.Console.WriteLine($"<{word}>");
        }
        return "prueba";
    }

    public static string LogLevel(string logLine)
    {
        return "caca";
    }

    public static string Reformat(string logLine)
    {
        return "caca";
    }
    static void Main(string[] args){
        Console.WriteLine("Hello World!");
    }
}

