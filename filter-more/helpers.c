#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int value = (image[i][j].rgbtBlue + image[i][j].rgbtRed + image[i][j].rgbtGreen)/3;
            image[i][j].rgbtBlue = value;
            image[i][j].rgbtRed = value;
            image[i][j].rgbtGreen = value;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < width/2; i++)
    {
        for (int j = 0; j < height; j++)
        {
            RGBTRIPLE temp = image[j][i];

            image[j][i].rgbtBlue = image[j][width-i].rgbtBlue;
            image[j][i].rgbtRed = image[j][width-i].rgbtRed;
            image[j][i].rgbtGreen = image[j][width-i].rgbtGreen;

            image[j][width-i].rgbtBlue = temp.rgbtBlue;
            image[j][width-i].rgbtRed = temp.rgbtRed;
            image[j][width-i].rgbtGreen = temp.rgbtGreen;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int red_sum = 0;
            red_sum += image[i][j].rgbtRed;
            red_sum += image[i-1][j-1].rgbtRed;
            red_sum += image[i-1][j].rgbtRed;
            red_sum += image[i][j-1].rgbtRed;
            red_sum += image[i-1][j+1].rgbtRed;
            red_sum += image[i+1][j-1].rgbtRed;
            red_sum += image[i+1][j].rgbtRed;
            red_sum += image[i][j+1].rgbtRed;
            red_sum += image[i+1][j+1].rgbtRed;


            int blue_sum = 0;
            blue_sum += image[i][j].rgbtBlue;
            blue_sum += image[i-1][j-1].rgbtBlue;
            blue_sum += image[i-1][j].rgbtBlue;
            blue_sum += image[i][j-1].rgbtBlue;
            blue_sum += image[i-1][j+1].rgbtBlue;
            blue_sum += image[i+1][j-1].rgbtBlue;
            blue_sum += image[i+1][j].rgbtBlue;
            blue_sum += image[i][j+1].rgbtBlue;
            blue_sum += image[i+1][j+1].rgbtBlue;


            int green_sum = 0;
            green_sum += image[i][j].rgbtGreen;
            green_sum += image[i-1][j-1].rgbtGreen;
            green_sum += image[i-1][j].rgbtGreen;
            green_sum += image[i][j-1].rgbtGreen;
            green_sum += image[i-1][j+1].rgbtGreen;
            green_sum += image[i+1][j-1].rgbtGreen;
            green_sum += image[i+1][j].rgbtGreen;
            green_sum += image[i][j+1].rgbtGreen;
            green_sum += image[i+1][j+1].rgbtGreen;

            int red_averege = red_sum / 9;
            int green_averege = green_sum / 9;
            int blue_averege = blue_sum / 9;

            image[i][j].rgbtRed = red_averege;
            image[i][j].rgbtBlue = blue_averege;
            image[i][j].rgbtGreen = green_averege;

            free()
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
