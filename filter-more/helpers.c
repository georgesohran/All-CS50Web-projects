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
            int blue_sum = 0;
            int green_sum = 0;

            if (i == 0 && j == 0)
            {
                red_sum += image[i][j].rgbtRed;
                red_sum += image[i+1][j].rgbtRed;
                red_sum += image[i][j+1].rgbtRed;
                red_sum += image[i+1][j+1].rgbtRed;

                blue_sum += image[i][j].rgbtBlue;
                blue_sum += image[i+1][j].rgbtBlue;
                blue_sum += image[i][j+1].rgbtBlue;
                blue_sum += image[i+1][j+1].rgbtBlue;

                green_sum += image[i][j].rgbtGreen;
                green_sum += image[i+1][j].rgbtGreen;
                green_sum += image[i][j+1].rgbtGreen;
                green_sum += image[i+1][j+1].rgbtGreen;

            }
            else if (i == 0 && j == width)
            {
                red_sum += image[i][j].rgbtRed;
                red_sum += image[i][j-1].rgbtRed;
                red_sum += image[i+1][j-1].rgbtRed;
                red_sum += image[i+1][j].rgbtRed;

                blue_sum += image[i][j].rgbtBlue;
                blue_sum += image[i][j-1].rgbtBlue;
                blue_sum += image[i+1][j-1].rgbtBlue;
                blue_sum += image[i+1][j].rgbtBlue;

                green_sum += image[i][j].rgbtGreen;
                green_sum += image[i][j-1].rgbtGreen;
                green_sum += image[i+1][j-1].rgbtGreen;
                green_sum += image[i+1][j].rgbtGreen;
            }
            else if (i == height && j == 0)
            {
                red_sum += image[i][j].rgbtRed;
                red_sum += image[i-1][j].rgbtRed;
                red_sum += image[i-1][j+1].rgbtRed;
                red_sum += image[i][j+1].rgbtRed;

                blue_sum += image[i][j].rgbtBlue;
                blue_sum += image[i-1][j].rgbtBlue;
                blue_sum += image[i-1][j+1].rgbtBlue;
                blue_sum += image[i][j+1].rgbtBlue;

                green_sum += image[i][j].rgbtGreen;
                green_sum += image[i-1][j].rgbtGreen;
                green_sum += image[i-1][j+1].rgbtGreen;
                green_sum += image[i][j+1].rgbtGreen;
            }
            else if (i == height && j == width)
            {
                red_sum += image[i][j].rgbtRed;
                red_sum += image[i-1][j-1].rgbtRed;
                red_sum += image[i-1][j].rgbtRed;
                red_sum += image[i][j-1].rgbtRed;

                blue_sum += image[i][j].rgbtBlue;
                blue_sum += image[i-1][j-1].rgbtBlue;
                blue_sum += image[i-1][j].rgbtBlue;
                blue_sum += image[i][j-1].rgbtBlue;

                green_sum += image[i][j].rgbtGreen;
                green_sum += image[i-1][j-1].rgbtGreen;
                green_sum += image[i-1][j].rgbtGreen;
                green_sum += image[i][j-1].rgbtGreen;
            }
            else if (i == 0 && j < width && j > 0)
            {
                red_sum += image[i][j].rgbtRed;
                red_sum += image[i][j-1].rgbtRed;
                red_sum += image[i+1][j-1].rgbtRed;
                red_sum += image[i+1][j].rgbtRed;
                red_sum += image[i][j+1].rgbtRed;
                red_sum += image[i+1][j+1].rgbtRed;

                blue_sum += image[i][j].rgbtBlue;
                blue_sum += image[i][j-1].rgbtBlue;
                blue_sum += image[i+1][j-1].rgbtBlue;
                blue_sum += image[i+1][j].rgbtBlue;
                blue_sum += image[i][j+1].rgbtBlue;
                blue_sum += image[i+1][j+1].rgbtBlue;

                green_sum += image[i][j].rgbtGreen;
                green_sum += image[i][j-1].rgbtGreen;
                green_sum += image[i+1][j-1].rgbtGreen;
                green_sum += image[i+1][j].rgbtGreen;
                green_sum += image[i][j+1].rgbtGreen;
                green_sum += image[i+1][j+1].rgbtGreen;
            }
            else if (i == height && j < width && j > 0)
            {
                red_sum += image[i][j].rgbtRed;
                red_sum += image[i-1][j-1].rgbtRed;
                red_sum += image[i-1][j].rgbtRed;
                red_sum += image[i][j-1].rgbtRed;
                red_sum += image[i-1][j+1].rgbtRed;
                red_sum += image[i][j+1].rgbtRed;

                blue_sum += image[i][j].rgbtBlue;
                blue_sum += image[i-1][j-1].rgbtBlue;
                blue_sum += image[i-1][j].rgbtBlue;
                blue_sum += image[i][j-1].rgbtBlue;
                blue_sum += image[i-1][j+1].rgbtBlue;
                blue_sum += image[i][j+1].rgbtBlue;

                green_sum += image[i][j].rgbtGreen;
                green_sum += image[i-1][j-1].rgbtGreen;
                green_sum += image[i-1][j].rgbtGreen;
                green_sum += image[i][j-1].rgbtGreen;
                green_sum += image[i-1][j+1].rgbtGreen;
                green_sum += image[i][j+1].rgbtGreen;
            }
            else if (j == 0 && i < height && i > 0)
            {
                red_sum += image[i][j].rgbtRed;
                red_sum += image[i-1][j].rgbtRed;
                red_sum += image[i-1][j+1].rgbtRed;
                red_sum += image[i+1][j].rgbtRed;
                red_sum += image[i][j+1].rgbtRed;
                red_sum += image[i+1][j+1].rgbtRed;

                blue_sum += image[i][j].rgbtBlue;
                blue_sum += image[i-1][j].rgbtBlue;
                blue_sum += image[i-1][j+1].rgbtBlue;
                blue_sum += image[i+1][j].rgbtBlue;
                blue_sum += image[i][j+1].rgbtBlue;
                blue_sum += image[i+1][j+1].rgbtBlue;

                green_sum += image[i][j].rgbtGreen;
                green_sum += image[i-1][j].rgbtGreen;
                green_sum += image[i-1][j+1].rgbtGreen;
                green_sum += image[i+1][j].rgbtGreen;
                green_sum += image[i][j+1].rgbtGreen;
                green_sum += image[i+1][j+1].rgbtGreen;
            }
            else if (j == width && i < height && i > 0)
            {
                red_sum += image[i][j].rgbtRed;
                red_sum += image[i-1][j-1].rgbtRed;
                red_sum += image[i-1][j].rgbtRed;
                red_sum += image[i][j-1].rgbtRed;
                red_sum += image[i+1][j-1].rgbtRed;
                red_sum += image[i+1][j].rgbtRed;

                blue_sum += image[i][j].rgbtBlue;
                blue_sum += image[i-1][j-1].rgbtBlue;
                blue_sum += image[i-1][j].rgbtBlue;
                blue_sum += image[i][j-1].rgbtBlue;
                blue_sum += image[i+1][j-1].rgbtBlue;
                blue_sum += image[i+1][j].rgbtBlue;

                green_sum += image[i][j].rgbtGreen;
                green_sum += image[i-1][j-1].rgbtGreen;
                green_sum += image[i-1][j].rgbtGreen;
                green_sum += image[i][j-1].rgbtGreen;
                green_sum += image[i+1][j-1].rgbtGreen;
                green_sum += image[i+1][j].rgbtGreen;
            }
            else
            {
                red_sum += image[i][j].rgbtRed;
                red_sum += image[i-1][j-1].rgbtRed;
                red_sum += image[i-1][j].rgbtRed;
                red_sum += image[i][j-1].rgbtRed;
                red_sum += image[i-1][j+1].rgbtRed;
                red_sum += image[i+1][j-1].rgbtRed;
                red_sum += image[i+1][j].rgbtRed;
                red_sum += image[i][j+1].rgbtRed;
                red_sum += image[i+1][j+1].rgbtRed;

                blue_sum += image[i][j].rgbtBlue;
                blue_sum += image[i-1][j-1].rgbtBlue;
                blue_sum += image[i-1][j].rgbtBlue;
                blue_sum += image[i][j-1].rgbtBlue;
                blue_sum += image[i-1][j+1].rgbtBlue;
                blue_sum += image[i+1][j-1].rgbtBlue;
                blue_sum += image[i+1][j].rgbtBlue;
                blue_sum += image[i][j+1].rgbtBlue;
                blue_sum += image[i+1][j+1].rgbtBlue;

                green_sum += image[i][j].rgbtGreen;
                green_sum += image[i-1][j-1].rgbtGreen;
                green_sum += image[i-1][j].rgbtGreen;
                green_sum += image[i][j-1].rgbtGreen;
                green_sum += image[i-1][j+1].rgbtGreen;
                green_sum += image[i+1][j-1].rgbtGreen;
                green_sum += image[i+1][j].rgbtGreen;
                green_sum += image[i][j+1].rgbtGreen;
                green_sum += image[i+1][j+1].rgbtGreen;
            }

            int red_averege = red_sum / 9;
            int green_averege = green_sum / 9;
            int blue_averege = blue_sum / 9;

            image[i][j].rgbtRed = red_averege;
            image[i][j].rgbtBlue = blue_averege;
            image[i][j].rgbtGreen = green_averege;
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int gx_red = 0;
            int gx_blue = 0;
            int gx_green = 0;

            int gy_red = 0;
            int gy_blue = 0;
            int gy_green = 0;

            if (i == 0 && j == 0)
            {
                gx_red += image[i][j].rgbtRed;
                gx_red += image[i+1][j].rgbtRed;
                gx_red += image[i][j+1].rgbtRed;
                gx_red += image[i+1][j+1].rgbtRed;

                gx_blue += image[i][j].rgbtBlue;
                gx_blue += image[i+1][j].rgbtBlue;
                gx_blue += image[i][j+1].rgbtBlue;
                gx_blue += image[i+1][j+1].rgbtBlue;

                gx_green += image[i][j].rgbtGreen;
                gx_green += image[i+1][j].rgbtGreen;
                gx_green += image[i][j+1].rgbtGreen;
                gx_green += image[i+1][j+1].rgbtGreen;


                gy_red += image[i][j].rgbtRed;
                gy_red += image[i+1][j].rgbtRed;
                gy_red += image[i][j+1].rgbtRed;
                gy_red += image[i+1][j+1].rgbtRed;

                gy_blue += image[i][j].rgbtBlue;
                gy_blue += image[i+1][j].rgbtBlue;
                gy_blue += image[i][j+1].rgbtBlue;
                gy_blue += image[i+1][j+1].rgbtBlue;

                gy_green += image[i][j].rgbtGreen;
                gy_green += image[i+1][j].rgbtGreen;
                gy_green += image[i][j+1].rgbtGreen;
                gy_green += image[i+1][j+1].rgbtGreen;

            }
            else if (i == 0 && j == width)
            {
                red_sum += image[i][j].rgbtRed;
                red_sum += image[i][j-1].rgbtRed;
                red_sum += image[i+1][j-1].rgbtRed;
                red_sum += image[i+1][j].rgbtRed;

                blue_sum += image[i][j].rgbtBlue;
                blue_sum += image[i][j-1].rgbtBlue;
                blue_sum += image[i+1][j-1].rgbtBlue;
                blue_sum += image[i+1][j].rgbtBlue;

                green_sum += image[i][j].rgbtGreen;
                green_sum += image[i][j-1].rgbtGreen;
                green_sum += image[i+1][j-1].rgbtGreen;
                green_sum += image[i+1][j].rgbtGreen;
            }
            else if (i == height && j == 0)
            {
                red_sum += image[i][j].rgbtRed;
                red_sum += image[i-1][j].rgbtRed;
                red_sum += image[i-1][j+1].rgbtRed;
                red_sum += image[i][j+1].rgbtRed;

                blue_sum += image[i][j].rgbtBlue;
                blue_sum += image[i-1][j].rgbtBlue;
                blue_sum += image[i-1][j+1].rgbtBlue;
                blue_sum += image[i][j+1].rgbtBlue;

                green_sum += image[i][j].rgbtGreen;
                green_sum += image[i-1][j].rgbtGreen;
                green_sum += image[i-1][j+1].rgbtGreen;
                green_sum += image[i][j+1].rgbtGreen;
            }
            else if (i == height && j == width)
            {
                red_sum += image[i][j].rgbtRed;
                red_sum += image[i-1][j-1].rgbtRed;
                red_sum += image[i-1][j].rgbtRed;
                red_sum += image[i][j-1].rgbtRed;

                blue_sum += image[i][j].rgbtBlue;
                blue_sum += image[i-1][j-1].rgbtBlue;
                blue_sum += image[i-1][j].rgbtBlue;
                blue_sum += image[i][j-1].rgbtBlue;

                green_sum += image[i][j].rgbtGreen;
                green_sum += image[i-1][j-1].rgbtGreen;
                green_sum += image[i-1][j].rgbtGreen;
                green_sum += image[i][j-1].rgbtGreen;
            }
            else if (i == 0 && j < width && j > 0)
            {
                red_sum += image[i][j].rgbtRed;
                red_sum += image[i][j-1].rgbtRed;
                red_sum += image[i+1][j-1].rgbtRed;
                red_sum += image[i+1][j].rgbtRed;
                red_sum += image[i][j+1].rgbtRed;
                red_sum += image[i+1][j+1].rgbtRed;

                blue_sum += image[i][j].rgbtBlue;
                blue_sum += image[i][j-1].rgbtBlue;
                blue_sum += image[i+1][j-1].rgbtBlue;
                blue_sum += image[i+1][j].rgbtBlue;
                blue_sum += image[i][j+1].rgbtBlue;
                blue_sum += image[i+1][j+1].rgbtBlue;

                green_sum += image[i][j].rgbtGreen;
                green_sum += image[i][j-1].rgbtGreen;
                green_sum += image[i+1][j-1].rgbtGreen;
                green_sum += image[i+1][j].rgbtGreen;
                green_sum += image[i][j+1].rgbtGreen;
                green_sum += image[i+1][j+1].rgbtGreen;
            }
            else if (i == height && j < width && j > 0)
            {
                red_sum += image[i][j].rgbtRed;
                red_sum += image[i-1][j-1].rgbtRed;
                red_sum += image[i-1][j].rgbtRed;
                red_sum += image[i][j-1].rgbtRed;
                red_sum += image[i-1][j+1].rgbtRed;
                red_sum += image[i][j+1].rgbtRed;

                blue_sum += image[i][j].rgbtBlue;
                blue_sum += image[i-1][j-1].rgbtBlue;
                blue_sum += image[i-1][j].rgbtBlue;
                blue_sum += image[i][j-1].rgbtBlue;
                blue_sum += image[i-1][j+1].rgbtBlue;
                blue_sum += image[i][j+1].rgbtBlue;

                green_sum += image[i][j].rgbtGreen;
                green_sum += image[i-1][j-1].rgbtGreen;
                green_sum += image[i-1][j].rgbtGreen;
                green_sum += image[i][j-1].rgbtGreen;
                green_sum += image[i-1][j+1].rgbtGreen;
                green_sum += image[i][j+1].rgbtGreen;
            }
            else if (j == 0 && i < height && i > 0)
            {
                red_sum += image[i][j].rgbtRed;
                red_sum += image[i-1][j].rgbtRed;
                red_sum += image[i-1][j+1].rgbtRed;
                red_sum += image[i+1][j].rgbtRed;
                red_sum += image[i][j+1].rgbtRed;
                red_sum += image[i+1][j+1].rgbtRed;

                blue_sum += image[i][j].rgbtBlue;
                blue_sum += image[i-1][j].rgbtBlue;
                blue_sum += image[i-1][j+1].rgbtBlue;
                blue_sum += image[i+1][j].rgbtBlue;
                blue_sum += image[i][j+1].rgbtBlue;
                blue_sum += image[i+1][j+1].rgbtBlue;

                green_sum += image[i][j].rgbtGreen;
                green_sum += image[i-1][j].rgbtGreen;
                green_sum += image[i-1][j+1].rgbtGreen;
                green_sum += image[i+1][j].rgbtGreen;
                green_sum += image[i][j+1].rgbtGreen;
                green_sum += image[i+1][j+1].rgbtGreen;
            }
            else if (j == width && i < height && i > 0)
            {
                red_sum += image[i][j].rgbtRed;
                red_sum += image[i-1][j-1].rgbtRed;
                red_sum += image[i-1][j].rgbtRed;
                red_sum += image[i][j-1].rgbtRed;
                red_sum += image[i+1][j-1].rgbtRed;
                red_sum += image[i+1][j].rgbtRed;

                blue_sum += image[i][j].rgbtBlue;
                blue_sum += image[i-1][j-1].rgbtBlue;
                blue_sum += image[i-1][j].rgbtBlue;
                blue_sum += image[i][j-1].rgbtBlue;
                blue_sum += image[i+1][j-1].rgbtBlue;
                blue_sum += image[i+1][j].rgbtBlue;

                green_sum += image[i][j].rgbtGreen;
                green_sum += image[i-1][j-1].rgbtGreen;
                green_sum += image[i-1][j].rgbtGreen;
                green_sum += image[i][j-1].rgbtGreen;
                green_sum += image[i+1][j-1].rgbtGreen;
                green_sum += image[i+1][j].rgbtGreen;
            }
            else
            {
                gx_red += image[i][j].rgbtRed * 0;
                gx_red += image[i-1][j-1].rgbtRed * -1;
                gx_red += image[i-1][j].rgbtRed * -2;
                gx_red += image[i][j-1].rgbtRed * 0;
                gx_red += image[i-1][j+1].rgbtRed * 0;
                gx_red += image[i+1][j-1].rgbtRed * 0;
                gx_red += image[i+1][j].rgbtRed * 0;
                gx_red += image[i][j+1].rgbtRed * 0;
                gx_red += image[i+1][j+1].rgbtRed * 0;

                gx_blue += image[i][j].rgbtBlue;
                gx_blue += image[i-1][j-1].rgbtBlue;
                gx_blue += image[i-1][j].rgbtBlue;
                gx_blue += image[i][j-1].rgbtBlue;
                gx_blue += image[i-1][j+1].rgbtBlue;
                gx_blue += image[i+1][j-1].rgbtBlue;
                gx_blue += image[i+1][j].rgbtBlue;
                gx_blue += image[i][j+1].rgbtBlue;
                gx_blue += image[i+1][j+1].rgbtBlue;

                gx_green += image[i][j].rgbtGreen;
                gx_green += image[i-1][j-1].rgbtGreen;
                gx_green += image[i-1][j].rgbtGreen;
                gx_green += image[i][j-1].rgbtGreen;
                gx_green += image[i-1][j+1].rgbtGreen;
                gx_green += image[i+1][j-1].rgbtGreen;
                gx_green += image[i+1][j].rgbtGreen;
                gx_green += image[i][j+1].rgbtGreen;
                gx_green += image[i+1][j+1].rgbtGreen;
            }

            int red_averege = red_sum / 9;
            int green_averege = green_sum / 9;
            int blue_averege = blue_sum / 9;

            image[i][j].rgbtRed = red_averege;
            image[i][j].rgbtBlue = blue_averege;
            image[i][j].rgbtGreen = green_averege;
        }
    }
    return;
}
