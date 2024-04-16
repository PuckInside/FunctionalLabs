#include <iostream>
#include <fstream>
#include <string>

std::string GetInput(std::string path)
{
    std::string line;
    std::ifstream in(path);

    if (in.is_open())
        std::getline(in, line);
    else
        line = "";

    in.close();
    return line;
}

void SendOutput(std::string path, bool output)
{
    std::ofstream out;
    out.open(path);

    if (out.is_open())
    {
        if (output)
            out << "YES" << std::endl;
        else
            out << "NO" << std::endl;
    }

    out.close();
}

bool IsHasNumber(std::string value)
{
    for (int i = 0; i <= 9; i++)
    {
        if (value.find('0' + i) != std::string::npos)
            return true;
    }

    return false;
}

bool IsHasUppercase(std::string value)
{
    for (int i = 0; i <= 25; i++)
    {
        if (value.find('A' + i) != std::string::npos)
            return true;
    }

    return false;
}

bool IsHasLowercase(std::string value)
{
    for (int i = 0; i <= 25; i++)
    {
        if (value.find('a' + i) != std::string::npos)
            return true;
    }

    return false;
}

bool IsCorrectFormat(std::string value)
{
    if (value.length() < 8)
        return false;

    if (!IsHasNumber(value))
        return false;

    if (!IsHasUppercase(value))
        return false;

    if (!IsHasLowercase(value))
        return false;

    return true;
}

int main()
{
    std::string nick = GetInput("input.txt");

    bool output = IsCorrectFormat(nick);

    SendOutput("output.txt" , output);

    return 0;
}