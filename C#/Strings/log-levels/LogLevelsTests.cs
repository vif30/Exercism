using Xunit;
using Exercism.Tests;

public class LogLevelsTests
{
    [Fact]
    [Task(1)]
    public void Error_message()
    {
        Assert.Equal("Stack overflow", LogLine.Message("[ERROR]: Stack overflow"));
    }

    [Fact]
    [Task(1)]
    public void Warning_message()
    {
        Assert.Equal("Disk almost full", LogLine.Message("[WARNING]: Disk almost full"));
    }

    [Fact]
    [Task(1)]
    public void Info_message()
    {
        Assert.Equal("File moved", LogLine.Message("[INFO]: File moved"));
    }

    [Fact]
    [Task(1)]
    public void Message_with_leading_and_trailing_white_space()
    {
        Assert.Equal("Timezone not set", LogLine.Message("[WARNING]:   \tTimezone not set  \r\n"));
    }
}