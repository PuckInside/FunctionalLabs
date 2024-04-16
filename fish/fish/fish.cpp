#include <iostream>
#include <fstream>
#include <string>
#include <vector>

std::vector<std::string> SplitString(std::string inputString)
{
    std::string currentWord;
    std::vector<std::string> words;

    for (char character : inputString)
    {
        if (character != ' ')
        {
            currentWord += character;
        }
        else
        {
            words.push_back(currentWord);
            currentWord = "";
        }
    }

    if (!currentWord.empty())
        words.push_back(currentWord);

    return words;
}

struct FishInfo
{
    float days = 0;
    float shelfLife = 0;
    std::vector<int> prices;
};

FishInfo GetInput(std::string path)
{
    std::string line;
    std::ifstream in(path);
    FishInfo info;

    if (in.is_open())
    {
        int allPrices = 0;

        std::getline(in, line);
        std::vector<std::string> words = SplitString(line);

        info.days = std::stoi(words[0]);
        info.shelfLife = std::stoi(words[1]);

        std::getline(in, line);
        std::vector<std::string> prices = SplitString(line);

        for (int i = 0; i < prices.size(); i++)
            info.prices.push_back(std::stoi(prices[i]));
    }
    else
    {
        info.days = 0;
        info.shelfLife = 0;
    }

    in.close();
    return info;
}

void SendOutput(std::string path, std::string output)
{
    std::ofstream out;
    out.open(path);

    if (out.is_open())
    {
        out << output << std::endl;
    }

    out.close();
}

int CurrentPurchase(std::vector<int> interval, int balance)
{
    int current = interval[0];
    int possible = 0;
    int buy = 0;

    for (int x : interval)
    {
        if (current <= x)
            possible++;
    }

    buy = possible - balance;
    if (buy <= 0)
        return 0;

    return buy;
}

std::vector<int> PurchaseForecast(FishInfo info)
{
    std::vector<int> purchases;
    int balance = 0;

    for (int i = 0; i < info.prices.size(); i++)
    {
        std::vector<int> interval;

        for (int j = 0; j < info.shelfLife; j++)
        {
            if (i + j == info.prices.size() - 1)
            {
                interval.push_back(info.prices[i + j]);
                break;
            }
            interval.push_back(info.prices[i + j]);
        }

        int current = CurrentPurchase(interval, balance);
        purchases.push_back(current);
        balance += current;
        balance--;
    }

    return purchases;
}

int CalculateCost(std::vector<int> prices, std::vector<int> buys)
{
    int cost = 0;

    for (int i = 0; i < prices.size(); i++)
    {
        cost += prices[i] * buys[i];
    }
    
    return cost;
}

int main()
{
    FishInfo info = GetInput("input.txt");
    std::vector<int> buys = PurchaseForecast(info);

    int cost = CalculateCost(info.prices, buys);

    std::string output;
    output = std::to_string(cost);
    output += "\n";
    for (int i = 0; i < buys.size(); i++)
    {
        output += std::to_string(buys[i]);
        output += " ";
    }


    std::cout << output;
    //SendOutput("output.txt", output);

    return 0;
}